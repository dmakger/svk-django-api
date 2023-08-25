class Validator:

    def __init__(self, queryset, error_adapter):
        self.queryset = queryset
        self.has_error = False
        self.error_adapter = error_adapter
        self.error = None

    def full(self):
        self.is_not_found()

        # if self.has_error:
        #     return self.error

    def is_not_found(self):
        if len(self.queryset) == 0:
            self.has_error = True
            self.error = self.error_adapter.is_not_found()
