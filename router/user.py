from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserBase, UserDisplay
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_user
from db.models import DbUser, DbProject
from sqlalchemy import func


router=APIRouter(
    prefix="/user",
    tags=['Users'],
    responses={404: {"description": "Not found"}},
)

# CREATE USER 
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=UserDisplay,summary="Create a new user",)
def create_user(request:UserBase,db:Session=Depends(get_db)):
    return db_user.create_user(db,request)


# GET ALL USERS
@router.get('/',status_code=status.HTTP_200_OK,response_model=list[UserDisplay],summary="Get all users",)
def get_all_users(db:Session=Depends(get_db)):
    return db_user.get_all_users(db)

# GET USER BY ID
@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=UserDisplay,summary="Get user by id",)
def get_user_by_id(id:int,db:Session=Depends(get_db)):
    return db_user.get_user_by_id(db,id)

# UPDATE USER BY ID
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,response_model=UserDisplay,summary="Update user by id",)
def update_user_by_id(id:int,request:UserBase,db:Session=Depends(get_db)):
    return db_user.update_user_by_id(db,id,request)

# DELETE USER BY ID
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT,summary="Delete user by id",)
def delete_user_by_id(id:int,db:Session=Depends(get_db)):
    return db_user.delete_user_by_id(db,id)

@router.get("/analytics/total_users")
def get_total_users_route(db: Session = Depends(get_db)):
    total_users = db.query(DbUser).count()
    total_projects = db.query(DbProject).count()
    return {"total_users": total_users, "total_projects": total_projects}


# @router.get("/summary")
# def get_user_summary(db: Session = Depends(get_db)):
#     # Use SQLAlchemy's func.sum to calculate the sum of user_id column
#     total = db.query(func.sum(DbProject.id).label("total")).scalar()
    
#     # db.close()
    
#     return {"total": total}
   