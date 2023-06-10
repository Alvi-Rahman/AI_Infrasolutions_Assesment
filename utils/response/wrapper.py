from utils.response.response_base import StatusCodeObject
from utils.response.status.codes import StatusCodes


class ResponseWrapper(StatusCodeObject, StatusCodes):
    def __init__(self, code: str, data: dict = None):
        # Traditional Way
        StatusCodes.__init__(self)
        if code.startswith('E'):
            response = self.get_error(code)
        else:
            response = self.get_success(code)
        response['data'] = data

        # New Way
        super(ResponseWrapper, self).__init__(**response)
