# app/models/ready_flag.py
from sqlalchemy import Column, String, Boolean
from app.config.db import Base

class ReadyEvent(Base):
    __tablename__ = "ready_event"

    team = Column(String, primary_key=True)  # "team1" or "team2"
    is_ready = Column(Boolean, default=False)