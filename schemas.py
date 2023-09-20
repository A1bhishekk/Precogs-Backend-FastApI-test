from pydantic import BaseModel
from typing import List

# article inside user display 
# class Article(BaseModel):
#     title: str
#     content: str
#     published: bool 
#     class Config:
#         orm_mode = True

# project inside user display 

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
    items:List[Project] = []
    class Config:
        orm_mode = True

class User(BaseModel):
    id:int
    username: str
    class Config:
        orm_mode = True

# class ArticleBase(BaseModel):
#     id:int
#     title: str
#     content: str
#     published: bool
#     creator_id: int
class ProjectBase(BaseModel):
    name:str
    github_url:str
    creator_id:int


# class ArticleDisplay(BaseModel):
#     id:int
#     title: str
#     content: str
#     published: bool
#     user:User
#     class Config:
#         orm_mode = True

class ProjectDisplay(BaseModel):
      id:int
      name:str
      github_url:str
      user:User
      class Config:
          orm_mode=True