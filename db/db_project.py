
from sqlalchemy.orm.session import Session
from schemas import ProjectBase
from db.models import DbProject


def create_project(db:Session,request:ProjectBase):
    new_project = DbProject(name=request.name,github_url=request.github_url,user_id=request.creator_id)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project

def get_project_by_id(db:Session,id:int):
    article = db.query(DbProject).filter(DbProject.id==id).first()
    return article


def get_all_projects(db:Session):
    projects = db.query(DbProject).all()
    return projects


