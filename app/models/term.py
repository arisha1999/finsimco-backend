from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.config.db import Base

class Term(Base):
    __tablename__ = "terms"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    value = Column(String)
    is_approved = Column(Boolean, default=False)