from pydantic import BaseModel
from typing import List
from datetime import datetime


class Project(BaseModel):
    id:int
    name:str
    github_url:str
    class Config:
        from_attributes = True


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
        from_attributes = True

class User(BaseModel):
    id:int
    username: str
    class Config:
        from_attributes = True


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
          from_attributes=True


class ScanBase(BaseModel):
    project_id: int
    line_of_code: int
    total_vul: int
    type_of_vul: str
    total_issues: int

class ScanDisplay(BaseModel):
    id: int
    project_id: int
    line_of_code: int
    total_vul: int
    type_of_vul: str
    total_issues: int
    created_at: datetime  # Add created_at field
    project:Project
    class Config:
        from_attributes = True