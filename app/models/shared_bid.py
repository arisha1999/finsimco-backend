from sqlalchemy import Column, Integer, String
from app.config.db import Base

class SharedBid(Base):
    __tablename__ = "shared_bid"

    id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    name = Column(String, unique=True)
    value = Column(String)