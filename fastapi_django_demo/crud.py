from fastapi_django_demo import fastapi_models
from fastapi_django_demo.models import Note


def get_notes(skip: int = 0, limit: int = 100):
    notes = list(Note.objects.all().order_by('id')[skip:limit])
    res = [get_note_from_db_model(note) for note in notes]
    return res


def create_note(note: fastapi_models.ApiNote):
    db_note = Note(**note.dict())
    db_note.save()
    return get_note_from_db_model(db_note)


def get_note_from_db_model(db_note: Note) -> fastapi_models.ApiNote:
    return fastapi_models.ApiNote(
        title=db_note.title,
        body=db_note.body,
        due=db_note.due,
        owner_id=db_note.owner.id
    )
