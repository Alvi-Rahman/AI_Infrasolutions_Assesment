"""
Module: feature_views.py
Description: This module contains Django views for managing features.

Dependencies:
- Django (django.contrib.gis.geos, django.http)
- drf_yasg (openapi, utils)
- rest_framework (permissions, generics, response)
- geoservice (features.models, features.serializers)
- utils (logger.Error, pagination.paginator, response.wrapper)

Classes:
- FeatureBaseAPIView: Base class for feature views. Provides common attributes and settings for feature views.
- FeatureListAPIView: View for listing features. Supports filtering by bounding box coordinates.
- FeatureRetrieveUpdateDestroyAPIView: View for retrieving, updating, and deleting a single feature.

"""

from django.contrib.gis.geos import Polygon
from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, generics
from rest_framework.response import Response

from geoservice.features.models import Feature
from geoservice.features.serializers import FeatureGeneralSerializer, FeatureUpdateSerializer
from utils.logger.Error import ErrorLogger
from utils.pagination.paginator import FeaturePagination
from utils.response.wrapper import ResponseWrapper


class FeatureBaseAPIView:
    """
    Base class for feature views. Provides common attributes and settings for feature views.
    """
    permission_classes = (permissions.IsAuthenticated,)
    response_wrapper = ResponseWrapper
    error_logger = ErrorLogger
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = Feature.objects.all()
    serializer_class = FeatureGeneralSerializer
    response_serializer_class = FeatureGeneralSerializer
    pagination_class = FeaturePagination
    lookup_field = 'id'


class FeatureListAPIView(FeatureBaseAPIView, generics.ListAPIView):
    """
    View for listing features. Supports filtering by bounding box coordinates.
    """

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('xmin', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
        openapi.Parameter('ymin', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
        openapi.Parameter('xmax', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
        openapi.Parameter('ymax', openapi.IN_QUERY, type=openapi.TYPE_NUMBER)
    ])
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a list of features.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - Response: The HTTP response containing the list of features.

        """
        try:
            self.get_serializer()
            response = super().get(request, *args, **kwargs)
            return Response(
                **self.response_wrapper('S207', response.data).formatted_output_success()
            )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500', request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )

    def get_queryset(self):
        """
        Get the queryset for retrieving the list of features.

        Returns:
        - queryset: The queryset for retrieving the list of features.
        """
        queryset = super().get_queryset()
        xmin = self.request.query_params.get('xmin')
        ymin = self.request.query_params.get('ymin')
        xmax = self.request.query_params.get('xmax')
        ymax = self.request.query_params.get('ymax')

        if xmin and ymin and xmax and ymax:
            bbox_polygon = Polygon.from_bbox((xmin, ymin, xmax, ymax))
            queryset = queryset.filter(features__intersects=bbox_polygon)
        return queryset


class FeatureRetrieveUpdateDestroyAPIView(FeatureBaseAPIView, generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating, and deleting a single feature.
    """

    serializer_class = FeatureUpdateSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a single feature.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - Response: The HTTP response containing the retrieved feature.

        """
        try:
            response = self.retrieve(request, *args, **kwargs)
            return Response(
                **self.response_wrapper('S208', response.data).formatted_output_success()
            )
        except Http404:
            return Response(
                **self.response_wrapper('E403').formatted_output_error()
            )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500', request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )

    def put(self, request, *args, **kwargs):
        """
        Handle PUT requests to update a single feature.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - Response: The HTTP response indicating the success of the update.

        """
        try:
            response = self.update(request, *args, **kwargs)
            return Response(
                **self.response_wrapper('S211', response.data).formatted_output_success()
            )
        except Http404:
            return Response(
                **self.response_wrapper('E403').formatted_output_error()
            )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500', request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )

    def patch(self, request, *args, **kwargs):
        """
        Handle PATCH requests to partially update a single feature.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - Response: The HTTP response indicating the success of the partial update.

        """
        try:
            response = self.partial_update(request, *args, **kwargs)
            return Response(
                **self.response_wrapper('S209', response.data).formatted_output_success()
            )
        except Http404:
            return Response(
                **self.response_wrapper('E403').formatted_output_error()
            )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500', request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE requests to delete a single feature.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - Response: The HTTP response indicating the success of the deletion.

        """
        try:
            response = self.destroy(request, *args, **kwargs)
            return Response(
                **self.response_wrapper('S210', response.data).formatted_output_success()
            )
        except Http404:
            return Response(
                **self.response_wrapper('E403').formatted_output_error()
            )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500', request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )
