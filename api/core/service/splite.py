from rest_framework import status
from rest_framework.response import Response

from .order import Order
from .paginator import Pagination
from .validator import Validator


class Splitting:
    def __init__(self, self_parent, request=None, qs=None, serializer_body=None):
        self.self_parent = self_parent
        self.request = request
        self.qs = qs
        self.serializer_body = serializer_body

        self.pagination = None
        self.serializer = None
        self.data = None
        self.response = None
        self.error = None


    def set(self, self_parent=None, request=None, qs=None):
        if self_parent is not None:
            self.self_parent = self_parent
        if request is not None:
            self.request = request
        if qs is not None:
            self.qs = qs

    # Проверка на валидность
    def validate(self):
        validator = Validator(self.qs, self.self_parent.error_adapter)
        validator.full()
        if validator.has_error:
            self.response = validator.error
            self.error = True

    # Сортировка
    def order_by(self):
        self.qs = Order.by(self.qs, self.request)

    # Пагинация
    def set_paginate(self):
        self.pagination = Pagination(request=self.request, queryset=self.qs)

    def paginate(self):
        self.data = self.pagination.get()
        self.data['results'] = self.serializer.data

    def serialize(self, my_qs=False, *args, **kwargs):
        kwargs = {**kwargs, **self.serializer_body}
        # if kwargs.get('instance') is None:
        #     kwargs['instance'] = self.qs
        if my_qs:
            args = [*args, self.qs]
        print(args, kwargs)
        self.serializer = self.self_parent.serializer_class(*args, **kwargs)
        self.data = self.serializer.data

    def complete(self, check_validate=True, check_order=True, check_paginate=True, check_serialize=True):
        if check_validate:
            self.validate()
            if self.error:
                return self.response
        if check_order:
            self.order_by()
        if check_paginate:
            self.set_paginate()
            if check_serialize:
                self.serialize(self.pagination.page_obj)
            self.paginate()
        if check_serialize and not check_paginate:
            self.serialize()

        return Response(self.data, status=status.HTTP_200_OK)

