from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserBase, UserDisplay
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_user
from db.models import DbUser, DbProject
from sqlalchemy import func
from starlette.responses import RedirectResponse
import httpx



router=APIRouter(
    prefix="/user",
    tags=['Users'],
    responses={404: {"description": "Not found"}},
)


Github_Client_ID= "1fb4439b6410513ba732"
Github_Client_Secret= "63dfcaffe8843d2de18493308b25baf3364b94f4"


# login with github
@router.get("/github-login")
async def github_login():
    return RedirectResponse(f"https://github.com/login/oauth/authorize?client_id={Github_Client_ID}",status_code=302)

# github callback
@router.get("/me",summary="Get user info",description="Get user info",)
async def github_callback(code:str):
    print(code)
    params={
        "client_id":Github_Client_ID,
        "client_secret":Github_Client_Secret,
        "code":code
    }
    headers={
        "Accept":"application/json",
        "Content-Type":"application/json"
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(url="https://github.com/login/oauth/access_token",params=params,headers=headers)
    response_json=response.json()
    access_token=response_json["access_token"]
    async with httpx.AsyncClient() as client:
        headers.update({"Authorization":f"Bearer {access_token}"})
        response = await client.get(url="https://api.github.com/user",headers=headers)
        github_data=response.json()
    return github_data

 

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
   