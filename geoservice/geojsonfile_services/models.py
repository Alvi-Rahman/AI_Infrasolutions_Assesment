from django.contrib.gis.db import models


class GeoJsonFiles(models.Model):
    name = models.CharField(max_length=100)
    geo_json_file = models.CharField(max_length=255)
    type_of_file = models.CharField(max_length=100, default='GeoJSON')
    crs = models.IntegerField(default=3857)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
