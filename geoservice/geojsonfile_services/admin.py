from django.contrib import admin
from geoservice.geojsonfile_services.models import *


class GeoJsonFilesAdmin(admin.ModelAdmin):
    list_display = ["id",
                    "name",
                    "geo_json_file",
                    "type_of_file",
                    "crs",
                    "created_at",
                    "updated_at",
                    ]
    search_fields = ["name", "type_of_file", "crs", ]


admin.site.register(GeoJsonFiles, GeoJsonFilesAdmin)
