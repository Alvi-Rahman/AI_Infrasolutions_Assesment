from django.urls import path, include
from geoservice.geojsonfile_services.urls import urlpatterns as geojsonfile_urls
from geoservice.features.urls import urlpatterns as feature_urls
from geoservice.frontend_views.urls import urlpatterns as frontend_urls

urlpatterns = [
    path('geo_json_files/', include(geojsonfile_urls)),
    path('main/', include(feature_urls)),
    path('', include(frontend_urls)),
]
