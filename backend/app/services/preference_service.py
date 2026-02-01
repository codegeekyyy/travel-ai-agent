from sqlalchemy.orm import Session
from app.models.preferences import TravelPreference

def get_user_preferences(db: Session, user_id: int):
    return db.query(TravelPreference).filter(
        TravelPreference.user_id == user_id
    ).first()