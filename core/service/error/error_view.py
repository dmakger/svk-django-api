from .error import ErrorHelper


class BrandPartnerError(ErrorHelper):
    def is_not_found(self):
        return self.get_error(error="Такого бренда не существует", status=self.NOT_FOUND)


class ArticleError(ErrorHelper):
    def is_not_found(self):
        return self.get_error(error="Такой статьи не существует", status=self.NOT_FOUND)
