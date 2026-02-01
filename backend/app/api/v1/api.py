from fastapi import APIRouter

api_router = APIRouter()

# import routes
from app.api.v1.auth import router as auth_router
from app.api.v1.preferences import router as preferences_router
from app.api.v1.agent import router as agent_router

# include routes
api_router.include_router(auth_router)
api_router.include_router(preferences_router)
api_router.include_router(agent_router)
