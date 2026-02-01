from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from jose import JWTError


# =========================
# JWT CONFIGURATION
# =========================

SECRET_KEY = "123456"        # move to .env in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# =========================
# PASSWORD HASHING (bcrypt)
# =========================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    """
    Hash plain password using bcrypt
    (used during signup)
    """
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify plain password against hashed password
    (used during login)
    """
    return pwd_context.verify(password, hashed_password)


# =========================
# JWT ACCESS TOKEN
# =========================

def create_access_token(data: dict) -> str:
    """
    Create JWT access token with expiry
    """
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


def decode_access_token(token: str):
    """
    Decode JWT token and return payload
    Returns None if token is invalid or expired
    """
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        return None
