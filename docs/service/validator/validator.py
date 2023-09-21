class Validator:

    def __init__(self, request=None, queryset=None, error_adapter=None):
        self.request = request
        self.queryset = queryset
        self.has_error = False
        self.error_adapter = error_adapter
        self.error = None

    def _get_queryset(self, queryset=None):
        if queryset is None:
            queryset = self.queryset
        if queryset is None:
            queryset = []
        return queryset

    def _get_request(self, request=None):
        if request is None:
            request = self.request
        return request

    def full(self):
        self.is_not_found()

        # if self.has_error:
        #     return self.error

    def is_not_found(self, queryset=None):
        queryset = self._get_queryset(queryset)
        if len(queryset) == 0:
            self.has_error = True
            self.error = self.error_adapter.is_not_found()

    def is_not_content(self, request=None, need_data=None):
        request = self._get_request(request)
        if request is None:
            return
        if need_data is None:
            need_data = []

        for el in request.data.get_all():
            pass
        # if len(self.queryset) == 0:
        #     self.has_error = True
        #     self.error = self.error_adapter.is_not_found()
