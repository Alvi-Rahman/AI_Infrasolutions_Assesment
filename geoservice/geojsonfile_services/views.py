"""
Module: geoservice.api.views

This module contains Django views for handling operations related to geo JSON files in a RESTFUL API.

Classes:
- GeoJsonBaseAPIView: Base class for API views.
- GeoJsonFileUploadView: View for uploading a geo JSON file.
- GeoJsonFileListView: View for listing geo JSON files.
- GeoJsonFileRetrieveView: View for retrieving a specific geo JSON file.
- GeoJsonFileDeleteView: View for deleting a geo JSON file.
- GeoJsonFileUpdateView: View for updating a geo JSON file.
- ImportFileToFeatures: View for importing a geo JSON file as features.

"""

from django.http import Http404
from rest_framework import parsers, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
import geopandas as gpd
import random
from django.contrib.gis.geos import GEOSGeometry

from geoservice.features.models import Feature
from geoservice.geojsonfile_services.models import GeoJsonFiles
from geoservice.geojsonfile_services.serializers import (GeoJsonFileUploadSerializer,
                                                         GeoJsonGeneralSerializer,
                                                         GeoJsonFilePatchSerializer)
from utils.geo_json_parser.upload_file import GeoFileUploader
from utils.logger.Error import ErrorLogger
from utils.pagination.paginator import FeaturePagination
from utils.response.wrapper import ResponseWrapper


class GeoJsonBaseAPIView(GenericAPIView):
    """
    Base class for API views.

    Attributes:
    - permission_classes: A tuple of permission classes required for authentication.
    - parser_classes: A tuple of parser classes for parsing request data.
    - response_wrapper: The response wrapper class for formatting API responses.
    - error_logger: The error logger class for logging unexpected errors.
    - http_method_names: A list of allowed HTTP methods.
    - queryset: The queryset for retrieving GeoJsonFiles objects.
    - serializer_class: The serializer class for serializing/deserializing data.
    - response_serializer_class: The serializer class for serializing response data.
    - pagination_class: The pagination class for paginating queryset results.
    - file_uploader: The file uploader class for uploading geo JSON files.
    - lookup_field: The lookup field for retrieving objects by a unique identifier.

    """

    permission_classes = (permissions.IsAuthenticated,)
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    response_wrapper = ResponseWrapper
    error_logger = ErrorLogger
    http_method_names = ["get", "post", "patch", "delete"]
    queryset = GeoJsonFiles.objects.all()
    serializer_class = GeoJsonGeneralSerializer
    response_serializer_class = GeoJsonGeneralSerializer
    pagination_class = FeaturePagination
    file_uploader = GeoFileUploader()
    lookup_field = 'id'


class GeoJsonFileUploadView(GeoJsonBaseAPIView):
    """
    View for uploading a geo JSON file.

    Attributes:
    - serializer_class: The serializer class for uploading a geo JSON file.

    Methods:
    - post: Handles the HTTP POST request for uploading a geo JSON file.

    """

    serializer_class = GeoJsonFileUploadSerializer

    def post(self, request, *args, **kwargs):
        """
        Handles the HTTP POST request for uploading a geo JSON file.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - response: The HTTP response.

        """
        try:
            serializer = self.get_serializer(data=request.data)

            if not serializer.is_valid():
                return Response(
                    **self.response_wrapper('E400').formatted_output_error()
                )

            geo_json_file = serializer.validated_data.pop("geo_json_file")
            file_upload_flag, response = self.file_uploader.upload(geo_json_file)

            if not file_upload_flag:
                self.error_logger.log_unexpected_error(response, dict(), 'E500',
                                                       request.get_full_path())
                return Response(
                    **self.response_wrapper('E401').formatted_output_error()
                )

            serializer.validated_data["geo_json_file"] = response
            serializer.save()
            return Response(
                        **self.response_wrapper(
                            'S201', self.response_serializer_class(serializer.validated_data).data).formatted_output_success()
                    )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500',
                                                   request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )


class GeoJsonFileListView(GeoJsonBaseAPIView):
    """
    View for listing geo JSON files.

    Methods:
    - get: Handles the HTTP GET request for listing geo JSON files.

    """

    def get(self, request, *args, **kwargs):
        """
        Handles the HTTP GET request for listing geo JSON files.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - response: The HTTP response.

        """
        try:
            queryset = self.filter_queryset(self.get_queryset())

            page = self.paginate_queryset(queryset)

            serializer = self.get_serializer(page, many=True)
            paginated_response = self.get_paginated_response(serializer.data).data
            return Response(
                **self.response_wrapper('S202', paginated_response).formatted_output_success()
            )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500',
                                                   request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )


class GeoJsonFileRetrieveView(GeoJsonBaseAPIView):
    """
    View for retrieving a specific geo JSON file.

    Methods:
    - get: Handles the HTTP GET request for retrieving a specific geo JSON file.

    """

    def get(self, request, *args, **kwargs):
        """
        Handles the HTTP GET request for retrieving a specific geo JSON file.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - response: The HTTP response.

        """
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(
                **self.response_wrapper('S203', serializer.data).formatted_output_success()
            )
        except Http404:
            return Response(
                **self.response_wrapper('E402').formatted_output_error()
            )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500',
                                                   request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )


class GeoJsonFileDeleteView(GeoJsonBaseAPIView):
    """
    View for deleting a geo JSON file.

    Methods:
    - delete: Handles the HTTP DELETE request for deleting a geo JSON file.

    """

    def delete(self, request, *args, **kwargs):
        """
        Handles the HTTP DELETE request for deleting a geo JSON file.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - response: The HTTP response.

        """
        try:
            instance = self.get_object()
            instance.delete()
            return Response(
                **self.response_wrapper('S204',
                                        {"data": f"{kwargs.get('id')} Successfully Deleted!"}
                                        ).formatted_output_success()
            )
        except Http404:
            return Response(
                **self.response_wrapper('E402').formatted_output_error()
            )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500',
                                                   request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )


class GeoJsonFileUpdateView(GeoJsonBaseAPIView):
    """
    View for updating a geo JSON file.

    Attributes:
    - serializer_class: The serializer class for updating a geo JSON file.

    Methods:
    - patch: Handles the HTTP PATCH request for updating a geo JSON file.

    """

    serializer_class = GeoJsonFilePatchSerializer

    def patch(self, request, *args, **kwargs):
        """
        Handles the HTTP PATCH request for updating a geo JSON file.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - response: The HTTP response.

        """
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response(
                    **self.response_wrapper('E400').formatted_output_error()
                )

            geo_json_file = serializer.validated_data.pop("geo_json_file", None)

            if geo_json_file:
                file_upload_flag, response = self.file_uploader.upload(geo_json_file)

                if not file_upload_flag:
                    self.error_logger.log_unexpected_error(response, dict(), 'E500',
                                                           request.get_full_path())
                    return Response(
                        **self.response_wrapper('E401').formatted_output_error()
                    )

                serializer.validated_data["geo_json_file"] = response

            serializer.save()

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(
                **self.response_wrapper('S205',
                                        serializer.validated_data
                                        ).formatted_output_success()
            )
        except Http404:
            return Response(
                **self.response_wrapper('E402').formatted_output_error()
            )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500',
                                                   request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )


class ImportFileToFeatures(GeoJsonBaseAPIView):
    """
    View for importing a geo JSON file as features.

    Methods:
    - get: Handles the HTTP GET request for importing a geo JSON file as features.

    """

    def get(self, request, *args, **kwargs):
        """
        Handles the HTTP GET request for importing a geo JSON file as features.

        Parameters:
        - request: The HTTP request object.
        - args: Additional positional arguments.
        - kwargs: Additional keyword arguments.

        Returns:
        - response: The HTTP response.

        """
        try:
            instance = self.get_object()
            gdf = gpd.read_file(instance.geo_json_file)
            gdf_values = gdf.values
            colors = ['red', 'green', 'blue', 'yellow']
            feature_lst = [
                Feature(
                    name=i[0],
                    features=GEOSGeometry(str(i[1])),
                    file_ref=instance,
                    color=random.choice(colors)
                ) for i in gdf_values
            ]

            _ = Feature.objects.bulk_create(feature_lst)

            return Response(
                **self.response_wrapper(
                    'S206', {"data": f"{kwargs.get('id')} Successfully Imported as Features!"}
                ).formatted_output_success()
            )
        except Http404:
            return Response(
                **self.response_wrapper('E402').formatted_output_error()
            )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500',
                                                   request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )
