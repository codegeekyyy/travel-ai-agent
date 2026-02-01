from fastapi import FastAPI
# from app.api.v1.auth import router as auth_router
# from app.api.v1.users import router as users_router
# from app.api.v1.preferences import router as preferences_router
from app.api.v1.api import api_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

# app.include_router(auth_router)
# app.include_router(users_router)
# app.include_router(preferences_router)
app.include_router(api_router)


@app.get("/health")
def health_check():
    return {"status": "OK"}
