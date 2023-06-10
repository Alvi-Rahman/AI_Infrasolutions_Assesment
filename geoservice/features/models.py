from django.contrib.gis.db import models


class Feature(models.Model):
    name = models.CharField(max_length=255)
    features = models.GeometryField(db_index=True)
    color = models.CharField(max_length=10, blank=True, null=True)
    file_ref = models.ForeignKey("geojsonfile_services.GeoJsonFiles",
                                 on_delete=models.SET_NULL,
                                 related_name='features', blank=True, null=True)
    edited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']
