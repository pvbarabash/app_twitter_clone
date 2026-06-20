from fastapi import FastAPI
from app.api.users import router as users_router

app = FastAPI(
    title="Twitter Clone API",
    version="1.0.0"
)

app.include_router(users_router)
