from datetime import date
from pydantic import BaseModel


class ApiNote(BaseModel):
    title: str
    body: str
    due: date
    owner_id: int
