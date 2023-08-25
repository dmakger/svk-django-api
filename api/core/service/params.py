# def paginate_and_serialize(serializer_class):
#     def decorator(view_func):
#         def wrapper(*args, **kwargs):
#             request = args[0].request  # Assuming the request is the first argument
#             qs = ...  # Replace with your queryset
#             result = Pagination(request=request, queryset=qs).get()
#             serializer = serializer_class(result.get('results'), many=True)
#             result['results'] = serializer.data
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# # Пример использования декоратора
# @paginate_and_serialize(serializer_class=YourSerializerClass)
# def your_view(request):
#     # Ваш код представления
#     pass
from functools import wraps

from rest_framework.exceptions import ValidationError

from .validator import Validator


def process_validator(func):
    @wraps(func)
    def wrapper(self, qs, *args, **kwargs):
        validator = Validator(qs, self.error_adapter)
        validator.full()
        if validator.has_error:
            return validator.error

    return wrapper


def validate(self, qs):
    validator = Validator(qs, self.error_adapter)
    validator.full()
    print(validator.has_error)

    if validator.has_error:
        return validator.error
    return
        # print('-----------')
        # raise ValidationError(validator.error)

    # def wrapper(self, request, **kwargs):
    #     # qs = self.get_qs(**kwargs)
    #     validator = Validator(qs, self.error_adapter)
    #     validator.full()
    #     print(validator.has_error)
    #
    #     if validator.has_error:
    #         # return validator.error
    #         print('-----------')
    #         raise ValidationError(validator.error)
    #
    #     return func(self, request, qs, **kwargs)
    #
    # return wrapper
