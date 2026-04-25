from datetime import datetime, timedelta, timezone

import bcrypt
from jose import jwt, JWTError

from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE, REFRESH_TOKEN_EXPIRE
from app.schemas.auth import AccessToken, RefreshToken

_ACCESS_TYPE = "access"
_REFRESH_TYPE = "refresh"


def _make_token(username: str, expires_in: timedelta, token_type: str) -> str:
    payload = {
        "sub": username,
        "type": token_type,
        "exp": datetime.now(timezone.utc) + expires_in,
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str, expected_type: str) -> str:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    if payload.get("type") != expected_type:
        raise JWTError(f"Expected token type '{expected_type}'")
    return payload["sub"]


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


def create_access_token(username: str) -> AccessToken:
    return AccessToken(
        access_token=_make_token(username, ACCESS_TOKEN_EXPIRE, _ACCESS_TYPE),
    )


def create_refresh_token(username: str) -> RefreshToken:
    return RefreshToken(
        access_token=_make_token(username, ACCESS_TOKEN_EXPIRE, _ACCESS_TYPE),
        refresh_token=_make_token(username, REFRESH_TOKEN_EXPIRE, _REFRESH_TYPE),
    )