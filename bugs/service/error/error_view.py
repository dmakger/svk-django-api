from .error import ErrorHelper


class BugRequestError(ErrorHelper):
    def is_not_content(self, data=None):
        return self.is_not_content_form(data)
