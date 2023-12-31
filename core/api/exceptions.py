from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler


def extra_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # If response is None, add more cases to the exception handler.
    if response is None:
        if isinstance(exc, IntegrityError):
            data = {'error': str(exc)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    return response


class GenericException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    detail = 'Error '

    def __init__(self, detail='Error', status_code=400):
        self.detail = detail
        self.status_code = status_code
