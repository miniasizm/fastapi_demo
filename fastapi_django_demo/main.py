from typing import List

from fastapi import APIRouter

from fastapi_django_demo import views
from fastapi_django_demo.fastapi_models import ApiNote


router = APIRouter()

router.post('/add-note/{user_id}/', response_model=ApiNote)(views.add_note)
router.get('/get-notes/', response_model=List[ApiNote])(views.get_notes)
