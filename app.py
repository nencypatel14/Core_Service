import os
import logging
from fastapi import FastAPI

from src.route.router import router

app = FastAPI(title="SMS_Service")
logging.basicConfig(level=logging.DEBUG)

# print env vars
logging.info("env vars: " + str(os.environ))

# Add route for APIs
app.include_router(router)


@app.get("/")
async def index():  
    return "SMS Service is running."
        