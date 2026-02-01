from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base

class TravelPreference(Base):
    __tablename__ = "travel_preferences"

    id = Column(Integer, primary_key=True, index= True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    
    travel_style = Column(String(50))      # budget / luxury
    transport_mode = Column(String(50))    # flight / train
    budget_range = Column(String(50))      # low / medium / high
    
    user = relationship("User", backref="preferences")