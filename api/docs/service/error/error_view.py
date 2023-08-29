from .error import ErrorHelper


class PageError(ErrorHelper):
    def is_not_found(self):
        return self.get_error(error="Такой страницы не существует", status=self.NOT_FOUND)
