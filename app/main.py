from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.users import router as users_router
from app.api.media import router as media_router

app = FastAPI(
    title="Twitter Clone API",
    version="1.0.0"
)

app.mount(
    "/media",
    StaticFiles(directory="media"),
    name="media",
)

app.include_router(users_router)

app.include_router(media_router)
