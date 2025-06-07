from sqlalchemy import Column, Integer, String
from app.config.db import Base

class Pricing(Base):
    __tablename__ = "pricing"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    name = Column(String, unique=True)
    value = Column(String)