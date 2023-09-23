from fastapi import FastAPI
from db import models
from db.database import engine
from router import user,project
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Precogs Backend API",
    description="This is a precogs api, with auto docs for the API and everything",
    version="0.1",
    docs_url="/",
)
app.include_router(user.router)
app.include_router(project.router)

# CORS
origins = [
    'http://localhost:3000',
    'http://localhost:8000',
    "https://github.com"
]


# add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(engine)
