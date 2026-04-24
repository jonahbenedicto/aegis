from sqlmodel import SQLModel


class UserCreate(SQLModel):
    email: str
    username: str
    name: str
    password: str


class UserRead(SQLModel):
    id: int
    email: str
    username: str
    name: str