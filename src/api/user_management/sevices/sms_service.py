import os
from config.config import setiings


class SmsService:
    def __init__(self, account_sid, auth_token):
            self.account_sid = setiings.ACCOUNT_SID
            self.auth_token = setiings.AUTH_TOKEN

    def send_sms(body: str, from_: str, to: int):
        """

        :param body:
        :param from_:
        :param to:
        :return:
        """
