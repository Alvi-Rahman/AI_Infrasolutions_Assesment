class SuccessCodes:
    def __init__(self):
        self.__success_dict = {
            "S200": self.default_success_response,
            "S201": self.geo_json_file_upload_success,
            "S202": self.geo_json_file_list_success,
            "S203": self.geo_json_file_retrieve_success,
            "S204": self.geo_json_file_delete_success,
            "S205": self.geo_json_file_update_success,
            "S206": self.data_insert_successful,
            "S207": self.feature_list_success,
            "S208": self.feature_retrieve_success,
            "S209": self.feature_update_success,
            "S210": self.feature_delete_success,
            "S211": self.log_out_success,
        }

    def get_success_dict(self):
        return self.__success_dict

    @property
    def get_default_success_dict(self):
        return self.__success_dict["S200"]

    @property
    def default_success_response(self):
        return dict(
            http_status=200,
            state_code="S200",
            state_message={
                "en": "Operation Successful"
            }
        )

    @property
    def geo_json_file_upload_success(self):
        return dict(
            http_status=201,
            state_code="S201",
            state_message={
                "en": "Geo Json File Creation Successful"
            }
        )

    @property
    def geo_json_file_list_success(self):
        return dict(
            http_status=200,
            state_code="S202",
            state_message={
                "en": "Geo Json List Data Fetch Success"
            }
        )

    @property
    def geo_json_file_retrieve_success(self):
        return dict(
            http_status=200,
            state_code="S203",
            state_message={
                "en": "Geo Json Data Retrieve Success"
            }
        )

    @property
    def geo_json_file_delete_success(self):
        return dict(
            http_status=200,
            state_code="S204",
            state_message={
                "en": "Geo Json Data Delete Success"
            }
        )

    @property
    def geo_json_file_update_success(self):
        return dict(
            http_status=200,
            state_code="S205",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def data_insert_successful(self):
        return dict(
            http_status=200,
            state_code="S206",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def feature_list_success(self):
        return dict(
            http_status=200,
            state_code="S207",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def feature_retrieve_success(self):
        return dict(
            http_status=200,
            state_code="S208",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def feature_update_success(self):
        return dict(
            http_status=200,
            state_code="S209",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def feature_delete_success(self):
        return dict(
            http_status=200,
            state_code="S210",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def log_out_success(self):
        return dict(
            http_status=200,
            state_code="S211",
            state_message={
                "en": "Successfully Logged Out"
            }
        )


