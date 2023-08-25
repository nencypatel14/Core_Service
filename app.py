import os
import logging
from fastapi import FastAPI

from src.route.router import router
from src.api.user_management.model.user_profile import UserProfile
from src.api.user_management.schema.user_profile_schema import UserProfile
from database.db import engine

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)

# print env vars
logging.info("env vars: " + str(os.environ))

# Add route for APIs
app.include_router(router)


@app.get("/")
async def index():
    return "SMS Service is running."
