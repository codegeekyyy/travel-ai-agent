from app.db.session import engine
from app.db.base import Base
from app.models.user import User  
import app.models  


def init_db():
    Base.metadata.create_all(bind=engine)
