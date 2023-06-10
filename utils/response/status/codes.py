from utils.response.status.error_codes import ErrorCodes
from utils.response.status.success_codes import SuccessCodes


class StatusCodes(SuccessCodes, ErrorCodes):
    def __init__(self):
        SuccessCodes.__init__(self)
        ErrorCodes.__init__(self)

    def get_error(self, code):
        return self.get_error_dict().get(code, self.get_default_error_dict)

    def get_success(self, code):
        return self.get_success_dict().get(code, self.get_default_success_dict)

