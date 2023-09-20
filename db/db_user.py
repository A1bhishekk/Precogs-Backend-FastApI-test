from sqlalchemy.orm.session import Session
from schemas import UserBase
from db.models import DbUser

def create_user(db:Session,request:UserBase):
    new_user = DbUser(username=request.username,email=request.email,github_id=request.github_id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_all_users(db:Session):
    users = db.query(DbUser).all()
    return users

def get_user_by_id(db:Session,id:int):
    user = db.query(DbUser).filter(DbUser.id==id).first()
    return user

def update_user_by_id(db:Session,id:int,request:UserBase):
    user = db.query(DbUser).filter(DbUser.id==id).first()
    user.username = request.username
    user.email = request.email
    user.github_id = request.github_id
    db.commit()
    db.refresh(user)
    return user

def delete_user_by_id(db:Session,id:int):
    user = db.query(DbUser).filter(DbUser.id==id).first()
    db.delete(user)
    db.commit()
    return "ok"

