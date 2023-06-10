from django.contrib.auth import logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from utils.auth.serializers import LogOutSerializer
from utils.logger.Error import ErrorLogger
from utils.response.wrapper import ResponseWrapper


class LogoutAPIView(APIView):
    response_wrapper = ResponseWrapper
    error_logger = ErrorLogger
    serializer_class = LogOutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(request_body=LogOutSerializer)
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                return Response(
                    **self.response_wrapper('E400').formatted_output_error()
                )
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            logout(request)
            return Response(
                **self.response_wrapper(
                    'S2012', {'data': 'success'}
                ).formatted_output_success()
            )
        except Exception as err:
            self.error_logger.log_unexpected_error(err, dict(), 'E500',
                                                   request.get_full_path())
            return Response(
                **self.response_wrapper('E500').formatted_output_error()
            )
