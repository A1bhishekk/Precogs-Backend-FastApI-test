from fastapi import APIRouter, Depends, HTTPException, status
from schemas import ProjectBase,ProjectDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_project


router=APIRouter(
    prefix="/project",
    tags=['Projects'],
)


# CREATE PROJECT
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=ProjectDisplay,summary="Create a new project",)
def create_project(request:ProjectBase,db:Session=Depends(get_db)):
    return db_project.create_project(db,request)


# GET PROJECT BY ID
@router.get('/{id}',status_code=status.HTTP_200_OK,response_model=ProjectDisplay,summary="Get article by id",)
def get_project_by_id(id:int,db:Session=Depends(get_db)):
    return db_project.get_project_by_id(db,id)

# GET ALL ARTICLES
@router.get('/',status_code=status.HTTP_200_OK,response_model=list[ProjectDisplay],summary="Get all projects",)
def get_projects(db:Session=Depends(get_db)):
    return db_project.get_all_projects(db)