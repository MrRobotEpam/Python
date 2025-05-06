from sqlalchemy import Column, Integer, String, Date, Boolean, DateTime
from datetime import datetime
from .database import Base

class Movie(Base):
    Movies = "movies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, 223, nullable=False)
    release_date = Column(Date, nullable=False)
    watched = Column(Boolean, default=False)
    status = Column(String, default="Active")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class RequestLogs (Base):
    Logs = "request_logs"

    id = Column(Integer, primary_key=True, index=True)
    method = Column(String, 10)
    endpoint = Column(String, 225)
    timestamp = Column(DateTime, default=datetime.utcnow)