from fastapi import FastAPI
import routers
import models
from config import Base, engine

app = FastAPI()

app.include_router(routers.auth_routers,tags=["Auth"])
app.include_router(routers.user_routers,tags=["User"])
app.include_router(routers.roles_router,tags=["Roles"])
app.include_router(routers.user_role_routers, tags=["User Roles"])
Base.metadata.create_all(bind=engine)

app.get("/")
async def homepage():
    return "Fastapi homepage"