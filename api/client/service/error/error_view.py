from .error import ErrorHelper


class ClientError(ErrorHelper):
    def is_not_found(self):
        return self.is_not_found_form("Такого клиента не существует")

    def is_not_content(self, data=None):
        return self.is_not_content_form(data)


class BusinessRequestError(ErrorHelper):
    def is_not_found(self):
        return self.is_not_found_form("Такого запроса клиента не существует")

    def is_not_found_curr(self, data=None):
        return self.is_not_found_form('По таким данным "Запроса клиента" не существует', data)

    def is_not_content(self, data=None):
        return self.is_not_content_form(data)
