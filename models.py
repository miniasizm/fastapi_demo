from datetime import datetime
from typing import List

from pydantic import BaseModel


class Image(BaseModel):
    name: str
    url: str


class Note(BaseModel):
    title: str
    body: str
    due: datetime
    owner_id: int
    attachments: List[Image]

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    notes: List[Note] = []

    class Config:
        orm_mode = True
