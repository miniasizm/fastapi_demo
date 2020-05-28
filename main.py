from typing import List

import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.graphql import GraphQLApp

import crud
import models
import sql_models
from database import engine, SessionLocal

sql_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class UserGraph(SQLAlchemyObjectType):
    class Meta:
        model = sql_models.User
        exclude_fields = ('hashed_password',)


class Query(graphene.ObjectType):
    users = graphene.List(UserGraph)

    def resolve_users(self, info):
        query = UserGraph.get_query(info)
        return query.all()


schema = graphene.Schema(query=Query)
app.add_route('/graph/', GraphQLApp(schema=schema))

@app.get('/')
async def root():
    return {'message': 'success'}


@app.get('/test/')
def test(test_var: int):
    return {'status': 'success'}


@app.post('/create-user/', response_model=models.User)
def create_user(user: models.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='User with that email is already registered.')
    return crud.create_user(db=db, user=user)


@app.post('/add-note/{user_id}/', response_model=models.Note)
async def add_note(note: models.Note, user_id: int, db: Session = Depends(get_db)):
    return crud.create_note(db=db, note=note, user_id=user_id)


@app.get('/get-notes/', response_model=List[models.Note])
def get_notes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    notes = crud.get_notes(db=db, skip=skip, limit=limit)
    return notes


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
