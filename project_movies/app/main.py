from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime
from . import database, models, schemas, services

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="ToWatchList API", version="1.0.0")

#------------------------------------------------------------------------------------
#DB Session dependency

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

#-------------------------------------------------------------------------------------
#Request logging decorator

def log_request(func):
    async def wrapper(*args, **kwargs):
        #args[0] is Request in path-op, depends on signature
        db: Session = kwargs["db"]
        db.add(models.RequestLogs(
            method=kwargs["request"].method,
            endpoint=kwargs["request"].url.path))
        db.commit()
        return await func (*args, **kwargs)
    return wrapper

#------------------------------------------------------------------------------------------
#Routes

from fastapi import Request

@app.get("/health", tags=["health"])
async def health():
    return {"status": "Ok", "timestamp": datetime.utcnow()}

@app.post("/movies", response_model=schemas.MovieDetail, status_code=201)
@log_request
async def add_movie(movie_in: schemas.MovieCreate,
                    request: Request,
                    db: Session = Depends(get_db)):
    service = services.MovieService(db)
    return service.create(movie_in)

@app.get("/movies", response_model=list[schemas.MovieOut])
@log_request
async def list_movies(request: Request, db: Session = Depends(get_db)):
    return services.MovieService(db). list()

@app.get("/movies/{movie_id}", response_model=schemas.MovieDetail)
@log_request
async def get_movie(movie_id: int,
                    request: Request,
                    db: Session = Depends(get_db)):
    svc = services.MovieService(db)
    movie = svc.get(movie_id)
    if not movie:
        raise HTTPException(404,"Movie Not Found")
    return movie

@app.patch("/movies/{movie_id}", response_model=schemas.MovieDetail)
@log_request
async def update_movie(movie_id: int,
                       data: schemas.MovieUpdate,
                       request: Request,
                       db: Session = Depends(get_db)):
    svc = services.MovieService(db)
    movie = svc.get(movie_id)
    if not movie:
        raise HTTPException(404, "Movie Not Found")
    return svc.update(movie, data)

@app.put("/movies/{movie_id}/watched", response_model=schemas.MovieDetail)
@log_request
async def mark_watched(movie_id: int,
                       request: Request,
                       db: Session = Depends(get_db)):
    svc = services.MovieService(db)
    movie = svc.get(movie_id)
    if not movie:
        raise HTTPException(404, "Moevie Not Found")
    return svc.mark_watched(movie)

@app.delete("/movies/{movie_id}",  status_code=204)
@log_request
async def delete_movie(movide_id: int,
                       request: Request,
                       db: Session = Depends(get_db)):
    svc = services.MovieService(db)
    movie = svc.get(movide_id)
    if not movie:
        raise HTTPException(404, "Movie Not Found")
    svc.soft_delete(movie)