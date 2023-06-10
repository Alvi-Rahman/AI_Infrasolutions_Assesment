from rest_framework_gis import serializers
from geoservice.features.models import Feature
from rest_framework import serializers as rest_serializers


class FeatureGeneralSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feature
        exclude = ('created_at', 'updated_at')


class FeatureUpdateSerializer(FeatureGeneralSerializer):
    name = rest_serializers.CharField(max_length=255, required=False, allow_null=True, allow_blank=True)
    features = serializers.GeometryField(required=False, allow_null=True)
    edited = rest_serializers.BooleanField(default=True)

    def validate(self, attrs):
        attrs['edited'] = True
        return super(FeatureUpdateSerializer, self).validate(attrs)
