from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.core.auth import get_current_user
from app.models.user import User
from app.models.preferences import TravelPreference
from app.schemas.preferences import PreferenceCreate

router = APIRouter(prefix="/preferences", tags=["Preferences"])

@router.post("/")
def save_preferences(
    data: PreferenceCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    pref = db.query(TravelPreference).filter(
        TravelPreference.user_id == current_user.id
    ).first()

    if pref:
        pref.travel_style = data.travel_style
        pref.transport_mode = data.transport_mode
        pref.budget_range = data.budget_range
    else:
        pref = TravelPreference(
            user_id=current_user.id,
            **data.dict()
        )
        db.add(pref)

    db.commit()
    return {"message": "Preferences saved"}
