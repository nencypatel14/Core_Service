from config.config import setting


class SmsService:
    def __init__(self, account_sid, auth_token):
            self.account_sid = setting.ACCOUNT_SID
            self.auth_token = setting.AUTH_TOKEN

    def send_sms(sms_body: str, from_mobile_number: str, to_mobile_number: int):
        """
        This function is use for send sms from 'from_mobile_number' number to 'to_mobile_number' number with 'sms_body'.
        :param sms_body:
        :param from_mobile_number:
        :param to_mobile_number:
        :return:
        """
        