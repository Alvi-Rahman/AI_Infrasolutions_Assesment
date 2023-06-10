from django.contrib import admin
from geoservice.features.models import Feature


class FeatureAdmin(admin.ModelAdmin):
    list_display = ["id",
                    "name",
                    "features",
                    "color",
                    "file_ref",
                    "edited",
                    "created_at",
                    "updated_at",
                    ]
    search_fields = ["name", "edited", ]


admin.site.register(Feature, FeatureAdmin)
