from fastapi import  APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.auth import get_current_user
from app.db.deps import get_db
from app.models.user import User
from app.schemas.agent import AgentRequest, AgentResponse
from app.agents.travel_agent import TravelAgent

router = APIRouter(prefix="/agent", tags=["AI Agent"])

agent = TravelAgent()

@router.post("/chat", response_model=AgentResponse)
def chat_with_agent(
    data: AgentRequest,
    current_user : User =Depends(get_current_user),
    db: Session = Depends(get_db),
):
    response = agent.run(
        user_id= current_user.id,
        query=data.query
    )

    return {"response": response}