import os
import logging
from fastapi import FastAPI
from typing_extensions import Annotated 
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends


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
        
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}