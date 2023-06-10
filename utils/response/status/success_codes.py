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
            "S2010": self.feature_delete_success,
            "S2011": self.feature_replace_success,
            "S2012": self.log_out_success,
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
            state_code="DSR2000",
            state_message={
                "en": "Geo Json File Creation Successful"
            }
        )

    @property
    def geo_json_file_upload_success(self):
        return dict(
            http_status=201,
            state_code="GJC2001",
            state_message={
                "en": "Geo Json File Creation Successful"
            }
        )

    @property
    def geo_json_file_list_success(self):
        return dict(
            http_status=200,
            state_code="GJL2002",
            state_message={
                "en": "Geo Json List Data Fetch Success"
            }
        )

    @property
    def geo_json_file_retrieve_success(self):
        return dict(
            http_status=200,
            state_code="GJR2003",
            state_message={
                "en": "Geo Json Data Retrieve Success"
            }
        )

    @property
    def geo_json_file_delete_success(self):
        return dict(
            http_status=200,
            state_code="GJD2004",
            state_message={
                "en": "Geo Json Data Delete Success"
            }
        )

    @property
    def geo_json_file_update_success(self):
        return dict(
            http_status=200,
            state_code="GJU2005",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def data_insert_successful(self):
        return dict(
            http_status=200,
            state_code="DIS2006",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def feature_list_success(self):
        return dict(
            http_status=200,
            state_code="FLS2007",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def feature_retrieve_success(self):
        return dict(
            http_status=200,
            state_code="FRS2008",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def feature_update_success(self):
        return dict(
            http_status=200,
            state_code="FUS2009",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def feature_delete_success(self):
        return dict(
            http_status=200,
            state_code="FDS2010",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def feature_replace_success(self):
        return dict(
            http_status=200,
            state_code="FRS2011",
            state_message={
                "en": "Geo Json Data Update Success"
            }
        )

    @property
    def log_out_success(self):
        return dict(
            http_status=200,
            state_code="LOS2012",
            state_message={
                "en": "Successfully Logged Out"
            }
        )


