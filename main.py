from fastapi import FastAPI
from db import models
from db.database import engine
from router import user,project

app = FastAPI(
    title="FastAPI with MySQL",
    description="This is a simple project to demonstrate FastAPI with MySQL",
    version="0.1",
    docs_url="/",
)
app.include_router(user.router)
# app.include_router(article.router)
app.include_router(project.router)






models.Base.metadata.create_all(engine)
