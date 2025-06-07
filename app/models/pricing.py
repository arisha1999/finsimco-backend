from sqlalchemy import Column, Integer, String
from app.config.db import Base

class Pricing(Base):
    __tablename__ = "pricing"

    id = Column(Integer, primary_key=True)
    company_name = Column(String)
    price = Column(Integer)
    shares = Column(Integer)