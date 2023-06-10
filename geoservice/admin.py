from django.contrib import admin
from geoservice.models import *


class ErrorLogsAdmin(admin.ModelAdmin):
    list_display = ["id",
                    "name",
                    "error_code",
                    "from_api",
                    "details",
                    "request_data",
                    "response_data",
                    "created_at",
                    "updated_at",
                    ]
    search_fields = ["name", "from_api", "error_code", ]


admin.site.register(ErrorLogs, ErrorLogsAdmin)
