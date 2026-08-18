from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class WorkplaceModel(Base):
    __tablename__ = 'workplaces'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    is_available = Column(Boolean, default=True)