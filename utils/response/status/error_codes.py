class ErrorCodes:
    def __init__(self, **kwargs):
        self.__error_dict = {
            "E400": self.data_validation_error,
            "E401": self.geo_json_file_upload_error,
            "E402": self.geo_json_file_invalid_id,
            "E403": self.feature_invalid_id,
            "E500": self.get_unknown_error
        }

    def get_error_dict(self) -> dict:
        return self.__error_dict

    @property
    def get_default_error_dict(self) -> dict:
        return self.__error_dict["E500"]

    @property
    def geo_json_file_upload_error(self):
        return dict(
            http_status=400,
            state_code="GJU4001",
            state_message={
                "en": "Geo Json File Upload Error."
            }
        )

    @property
    def data_validation_error(self):
        return dict(
            http_status=400,
            state_code="DVE4000",
            state_message={
                "en": "Data Validation Error."
            }
        )

    @property
    def geo_json_file_invalid_id(self):
        return dict(
            http_status=400,
            state_code="GJI4002",
            state_message={
                "en": "Invalid Id Given."
            }
        )

    @property
    def feature_invalid_id(self):
        return dict(
            http_status=400,
            state_code="FII4003",
            state_message={
                "en": "Invalid Feature Id Given."
            }
        )

    @property
    def get_unknown_error(self):
        return dict(
            http_status=400,
            state_code="UNK5000",
            state_message={
                "en": "Something Went Wrong."
            }
        )
