from sqlalchemy.orm import Session

import models
import sql_models


def get_user(db: Session, user_id: int):
    return db.query(sql_models.User).filter(sql_models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(sql_models.User).filter(sql_models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: models.UserCreate):
    fake_hash = user.password + "TODO"
    db_user = sql_models.User(email=user.email, hashed_password=fake_hash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_models.Note).offset(skip).limit(limit).all()


def create_note(db: Session, note: models.Note, user_id: int):
    db_note = sql_models.Note(**note.dict(), owner_id=user_id)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note
