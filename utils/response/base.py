class BaseCodeObject(object):
    def __init__(self, **kwargs):
        self._http_status = kwargs.get('http_status', 500)
        self._state_code = kwargs.get('state_code', 'BASE_CODE_500')
        self._state_message = kwargs.get('state_message', {'en': 'No message defined'})
        self._state_message_params = kwargs.get("state_message_params", {})
        self._response_data = kwargs.get("data", {})

    def http_status(self) -> int:
        return self._http_status

    def set_http_status(self, status):
        self._http_status = status

    def state_code(self) -> str:
        return self._state_code

    def set_state_code(self, state_code):
        self._state_code = state_code

    def state_message(self) -> dict:
        return self._state_message

    def set_state_message(self, message):
        self._state_message = message

    def state_message_params(self) -> dict:
        return self._state_message_params

    def set_state_message_params(self, params):
        self._state_message_params = params

    def get_data(self) -> dict:
        return self._response_data

    def set_data(self, data):
        self._response_data = data

    def is_http_error_status(self) -> bool:
        return 400 <= self._http_status <= 599

    def is_http_success_status(self) -> bool:
        return 200 <= self._http_status <= 299

    def deep_copy(self):
        return BaseCodeObject(
            http_status=self.http_status(),
            state_code=self.state_code(),
            state_message=self.state_message(),
            state_message_params=self.state_message_params()
        )
