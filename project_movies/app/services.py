from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

class MovieService:
    def __init__(self, db: Session):
        self.db = db
    
    #---------CRUD--------------------------------------------------------
    def create(self, movie_in: schemas.MovieCreate) -> models.Movie:
        movie = models.Movie(**movie_in.dict())
        self.db.add(movie)
        self.db.commit()
        self.db.refresh(movie)
        return movie
    
    def list(self) -> list[models.Movie]:
        return (self.db.query(models.Movie)
                .filter(models.Movie.status == "ACTIVE")
                .all())
    
    def get(self, movie_id: int) -> models.Movie | None:
        return self.db.query(models.Movie).filter(
            models.Movie.id == movie_id,
            models.Movie.status == "ACTIVE"
        ).first()
    
    def update (self, movie: models.Movie, data: schemas.MovieUpdate) -> models.Movie:
        for field, value in data.dict(exclude_unset=True).items():
            setattr(movie, field, value)
        self.db.commit()
        self.db.refresh(movie)
        return movie
    
    def mark_watched(self, movie: models.Movie) -> models.Movie:
        movie.watched = True
        self.db.commit()
        self.db.refresh(movie)
        return movie
    
    def soft_delete(self, movie: models.Movie):
        movie.status = "DELETED"
        self.db.commit()
    

