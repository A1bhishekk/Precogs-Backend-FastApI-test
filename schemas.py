from pydantic import BaseModel
from typing import List
from datetime import datetime


class Project(BaseModel):
    id:int
    name:str
    github_url:str
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    github_id: int

class UserDisplay(BaseModel):
    id:int
    username: str
    email: str
    github_id: int
    created_at: datetime  # Add created_at field
    projects:List[Project] = []
    class Config:
        orm_mode = True

class User(BaseModel):
    id:int
    username: str
    class Config:
        orm_mode = True


class ProjectBase(BaseModel):
    name:str
    github_url:str
    creator_id:int



class ProjectDisplay(BaseModel):
      id:int
      name:str
      github_url:str
      created_at: datetime  # Add created_at field
      user:User
      class Config:
          orm_mode=True


