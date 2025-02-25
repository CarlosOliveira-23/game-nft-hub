from rest_framework.response import Response
from rest_framework import status


class ResponseHandler:
    """ Class to standardize API responses """

    @staticmethod
    def success(data, message="Success", status_code=status.HTTP_200_OK):
        return Response({
            "status": "success",
            "message": message,
            "data": data
        }, status=status_code)

    @staticmethod
    def error(message="An error occurred", status_code=status.HTTP_400_BAD_REQUEST):
        return Response({
            "status": "error",
            "message": message
        }, status=status_code)
