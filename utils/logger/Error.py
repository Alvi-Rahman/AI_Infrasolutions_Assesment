from geoservice.models import ErrorLogs


class ErrorLogger:
    @classmethod
    def log_unexpected_error(cls, error: Exception, request_data: dict,
                             code: str, from_api: str):
        _ = ErrorLogs.objects.create(
            name=type(error),
            error_code=code,
            from_api=from_api,
            details=error.args[0],
            request_data=request_data
        )
        return True
