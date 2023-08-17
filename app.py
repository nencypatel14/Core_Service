import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.api.user_management.sevices.sms_service import SmsService
from src.api.user_management.schema.sms import SmsInput
from config.config import setiings
import uvicorn


app = FastAPI()
logging.basicConfig(level=logging.INFO)


@app.post("/send/user_management")
async def send_sms(input_sms: SmsInput):
    try:

        # logging.debug("This is Debug message")
        logging.info("check your Account Sid and auth token are available.")
        # logging.error("error message")
        # logging.warning("This is Warning message")
        # logging.critical("Critical message")

        if not input_sms.number:
            logging.warning("account_sid or auth_token is missing")

        SmsService.send_sms(body=input_sms.message, from_= setiings.FROM_MOBILE_NUMBER, to = input_sms.number)
        print(input_sms.__dict__)
        return JSONResponse(input_sms.__dict__)
    except ArithmeticError as e:
        print(e)

