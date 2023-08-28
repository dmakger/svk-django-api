from rest_framework import status as st
from rest_framework.response import Response


class ErrorHelper:
    NOT_FOUND = st.HTTP_404_NOT_FOUND
    NOT_CONTENT = st.HTTP_204_NO_CONTENT

    @staticmethod
    def is_not_found_form(message, data=None):
        if data is not None:
            message = f"{message} ({', '.join(data)})"
        return ErrorHelper.get_error(error=message, status=ErrorHelper.NOT_FOUND)

    @staticmethod
    def is_not_content_form(data=None):
        message = "Переданы не все аргументы"
        if data is not None:
            message = f"{message} ({', '.join(data)})"
        return ErrorHelper.get_error(error=message, status=ErrorHelper.NOT_CONTENT)

    @staticmethod
    def get_error(error: str, status: int):
        return Response(
            {'error': error},
            status=status,
        )
