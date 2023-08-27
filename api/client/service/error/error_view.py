from .error import ErrorHelper


class ClientError(ErrorHelper):
    def is_not_found(self):
        return self.get_error(error="Такого клиента не существует не существует", status=self.NOT_FOUND)

    def is_not_content(self, data=None):
        message = "Переданы не все аргументы"
        if data is not None:
            message = f"{message} ({', '.join(data)})"
        return self.get_error(error=message, status=self.NOT_CONTENT)

