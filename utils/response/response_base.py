from utils.response.base import BaseCodeObject


class StatusCodeObject(BaseCodeObject):
    def __init__(self, **kwargs):
        super(StatusCodeObject, self).__init__(**kwargs)

    def get_status_code(self) -> int:
        return self.http_status()

    def get_state_code(self) -> str:
        return self.state_code()

    def get_state_message(self, language: str = 'en') -> str:
        data: dict = self.state_message()
        if language in data:
            return data.get(language)
        else:
            return data.get('en', '')

    def formatted_output_error(self, language: str = 'en') -> dict:
        if not self.is_http_error_status():
            raise ValueError('the http status code is not in error range')
        output = dict()
        output['status'] = self.get_status_code()
        output['data'] = {}
        output['data']['code'] = self.get_state_code()
        output['data']['message'] = self.get_state_message(language)
        output['data']['lang'] = language
        return output

    def formatted_output_success(self, language: str = 'en') -> dict:
        if not self.is_http_success_status():
            raise ValueError('the http status code is not in success range')
        output = dict()
        output['status'] = self.get_status_code()
        output['data'] = {}

        output['data']['code'] = self.get_state_code()
        output['data']['lang'] = language
        output['data']['message'] = self.get_state_message(language)
        output['data']['data'] = self.get_data()
        return output
