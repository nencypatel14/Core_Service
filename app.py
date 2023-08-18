import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from config.config import setiings
from src.api.user_management.sevices.sms_service import SmsService
from src.api.user_management.schema.sms import SmsInput


app = FastAPI()
logging.basicConfig(level=logging.INFO)


@app.get("/")
async def index():
    return "SMS Service is running."


@app.post("/send/user-management")
async def send_sms(input_sms: SmsInput):
    try:

        if not input_sms.number:
            logging.warning("account_sid or auth_token is missing")

        SmsService.send_sms(body=input_sms.message, from_= setiings.FROM_MOBILE_NUMBER, to = input_sms.number)
        print(input_sms.__dict__)
        return JSONResponse(input_sms.__dict__)
    except ArithmeticError as e:
        print(e)

