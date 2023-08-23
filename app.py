import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from config.config import setting
from src.api.user_management.sevices.sms_service import SmsService
from src.api.user_management.schema.sms import SmsInput
from src.api.user_management.model.user_sms_model import session
import psycopg2 as db

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

        SmsService.send_sms(body=input_sms.message, from_= setting.FROM_MOBILE_NUMBER, to = input_sms.number)
        # print(input_sms.__dict__)

        # cursor = conn.cursor()

        # cursor.execute(insert_query, (input_sms.message, input_sms.number))
        # conn.commit()

        session.commit()
        # cursor.close()
        return JSONResponse(input_sms.__dict__)
    except ArithmeticError as e:
        print(e)
