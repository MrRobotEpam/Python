from datetime import date, datetime
from pydantic import BaseModel, Field

class MovieBase(BaseModel):
    name: str = Field(..., example="Interestellar")
    release_date = date = Field(..., example="2014-11-07")

class MovieCreate(MovieBase):
    pass

class MovieUpdate(BaseModel):
    name: str | None = None
    release_date = date | None = None

class MovieOut(MovieBase):
    id: int
    watched: bool
    class config:
        orm_mode = True

class MovieDetail(MovieOut):
    created_at = datetime
    updated_at = datetime
    status: str

