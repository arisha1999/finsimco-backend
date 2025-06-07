from sqlalchemy import Column, Integer, String
from app.config.db import Base

class SharedBid(Base):
    __tablename__ = "shared_bid"

    id = Column(Integer, primary_key=True)
    investor_name = Column(String)
    company_name = Column(String)
    bid = Column(Integer)