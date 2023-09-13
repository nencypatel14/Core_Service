import logging
from fastapi.responses import JSONResponse

from app import app
from config.config import setting
from src.api.user_management.sevices.sms_service import SmsService
from src.api.user_management.schema.sms_service_schema import SmsInput


@app.post("/send/user-management")
async def send_sms(input_sms: SmsInput):
    try:
        if not input_sms.number:
            logging.warning("account_sid or auth_token is missing")

        SmsService.send_sms(body=input_sms.message, from_= setting.FROM_MOBILE_NUMBER, to = input_sms.number)
        return JSONResponse(input_sms.__dict__)
    except ArithmeticError as e:
        logging.error(f"Error - send_sms: {e}")
        raise Exception("internal_sever_error")
    
