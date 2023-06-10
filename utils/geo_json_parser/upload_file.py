import os
from AiInfraSolutions.settings import GEO_FILE_LOCATION


class GeoFileUploader:
    def __init__(self):
        self.location = GEO_FILE_LOCATION
        self.file_type = 'GeoJson'

    def upload(self, file):
        try:
            destination = open(os.path.join(self.location, file.name), 'wb+')
            for chunk in file.chunks():
                destination.write(chunk)
            destination.close()

            return True, os.path.join(self.location, file.name)
        except Exception as error:
            return False, error
