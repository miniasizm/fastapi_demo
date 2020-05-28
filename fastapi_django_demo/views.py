from typing import List

from fastapi_django_demo import crud
from fastapi_django_demo.fastapi_models import ApiNote


def add_note(note: ApiNote) -> ApiNote:
    return crud.create_note(note=note)


def get_notes(skip: int = 0, limit: int = 100) -> List[ApiNote]:
    notes = crud.get_notes(skip=skip, limit=limit)
    return notes
