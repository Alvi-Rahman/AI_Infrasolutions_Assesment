from rest_framework import serializers

from geoservice.geojsonfile_services.models import GeoJsonFiles


class GeoJsonGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoJsonFiles
        exclude = ('created_at', 'updated_at')


class GeoJsonFileUploadSerializer(GeoJsonGeneralSerializer):
    geo_json_file = serializers.FileField()


class GeoJsonFilePatchSerializer(GeoJsonGeneralSerializer):
    geo_json_file = serializers.FileField(allow_empty_file=True, allow_null=True, required=False)
    name = serializers.CharField(max_length=100, required=False, allow_blank=True, allow_null=True)


