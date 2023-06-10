from django.urls import path
from geoservice.geojsonfile_services.views import (
    GeoJsonFileUploadView, GeoJsonFileListView, GeoJsonFileRetrieveView,
    GeoJsonFileDeleteView, GeoJsonFileUpdateView, ImportFileToFeatures
)

urlpatterns = [
    path('upload_geo_json_files/', GeoJsonFileUploadView.as_view()),
    path('list_geo_json_files/', GeoJsonFileListView.as_view()),
    path('get_geo_json_files/<int:id>', GeoJsonFileRetrieveView.as_view()),
    path('delete_geo_json_files/<int:id>', GeoJsonFileDeleteView.as_view()),
    path('update_geo_json_files/<int:id>', GeoJsonFileUpdateView.as_view()),
    path('import_geo_json_file_to_features/<int:id>', ImportFileToFeatures.as_view()),
]
