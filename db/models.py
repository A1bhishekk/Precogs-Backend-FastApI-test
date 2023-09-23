# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
# from db.database import Base
# from sqlalchemy.orm import relationship


# class DbUser(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50))
#     github_id = Column(Integer, unique=True)
#     email = Column(String(50), unique=True)
#     items = relationship("DbProject",back_populates="user")  # relationship to projects table
   
   

# class DbProject(Base):
#     __tablename__='projects'
#     id = Column(Integer, primary_key=True, index=True)
#     name=Column(String(50))
#     github_url=Column(String(50))
#     user_id=Column(Integer, ForeignKey('users.id'))

#     user=relationship("DbUser",back_populates="items") 



    




# # class DbArticle(Base):
# #     __tablename__ = 'articles'
# #     id = Column(Integer, primary_key=True, index=True)
# #     title = Column(String(50))
# #     content=Column(String(50))
# #     published=Column(Boolean)
# #     user_id = Column(Integer, ForeignKey('users.id'))   # foreign key to users table

# #     user=relationship("DbUser",back_populates="items")  # relationship to users table 


# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
# from db.database import Base
# from sqlalchemy.orm import relationship, backref

# class DbUser(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50))
#     github_id = Column(Integer, unique=True)
#     email = Column(String(50), unique=True)
#     items = relationship(
#         "DbProject",
#         back_populates="user",
#         cascade="all, delete-orphan"  # Add this line for cascading deletion
#     )

# class DbProject(Base):
#     __tablename__ = 'projects'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(50))
#     github_url = Column(String(50))
#     user_id = Column(Integer, ForeignKey('users.id'))

#     user = relationship(
#         "DbUser",
#         back_populates="items",
#         # Optionally, you can add a "cascade" option here as well if needed.
#     )



# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
# from db.database import Base
# from sqlalchemy.orm import relationship, backref
# from datetime import datetime

# class DbUser(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50))
#     github_id = Column(Integer, unique=True)
#     email = Column(String(50), unique=True)
#     created_at = Column(DateTime, default=datetime.utcnow)  # Added created_at column

#     items = relationship(
#         "DbProject",
#         back_populates="user",
#         cascade="all, delete-orphan"  # Add this line for cascading deletion
#     )

# class DbProject(Base):
#     __tablename__ = 'projects'
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(50))
#     github_url = Column(String(50))
#     user_id = Column(Integer, ForeignKey('users.id'))
#     created_at = Column(DateTime, default=datetime.utcnow)  # Added created_at column

#     user = relationship(
#         "DbUser",
#         back_populates="items",
#         # Optionally, you can add a "cascade" option here as well if needed.
#     )


from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from db.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func  # Import func for handling timestamps

class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    github_id = Column(Integer, unique=True)
    email = Column(String(50), unique=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)  # Automatic creation timestamp

    projects = relationship(
        "DbProject",
        back_populates="user",
        cascade="all, delete-orphan"
    )

class DbProject(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    github_url = Column(String(50))
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)  # Automatic creation timestamp

    user = relationship(
        "DbUser",
        back_populates="projects"
    )
