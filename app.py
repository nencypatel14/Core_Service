import os
import logging
from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware

from src.route.router import router

app = FastAPI(title="Core_Service")
logging.basicConfig(level=logging.DEBUG)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/user-management/user/token")


# print env vars
logging.info("env vars: " + str(os.environ))

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add route for APIs
app.include_router(router)
        