from pydantic import BaseModel


class PreferenceCreate(BaseModel):
    travel_style: str
    transport_mode: str
    budget_range: str


class PreferenceResponse(PreferenceCreate):
    id: int

    class config:
        from_attributes = True