from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from db.database import Base
from sqlalchemy.orm import relationship


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    github_id = Column(Integer, unique=True)
    email = Column(String(50), unique=True)
    items = relationship("DbProject",back_populates="user")  # relationship to projects table
   


# class DbArticle(Base):
#     __tablename__ = 'articles'
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(50))
#     content=Column(String(50))
#     published=Column(Boolean)
#     user_id = Column(Integer, ForeignKey('users.id'))   # foreign key to users table

#     user=relationship("DbUser",back_populates="items")  # relationship to users table    

class DbProject(Base):
    __tablename__='projects'
    id = Column(Integer, primary_key=True, index=True)
    name=Column(String(50))
    github_url=Column(String(50))
    user_id=Column(Integer, ForeignKey('users.id'))

    user=relationship("DbUser",back_populates="items") 



    