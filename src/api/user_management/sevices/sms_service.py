import os
from config.config import setting


class SmsService:
    def __init__(self, account_sid, auth_token):
            self.account_sid = setting.ACCOUNT_SID
            self.auth_token = setting.AUTH_TOKEN

    def send_sms(body: str, from_: str, to: int):
        """

        :param body:
        :param from_:
        :param to:
        :return:
        """
