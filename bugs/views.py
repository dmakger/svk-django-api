from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from _service.mail.handler import MailHandler
from _service.mail.mail import Mail
from bugs.models import Bug
from bugs.serializers import BugSerializer
from bugs.service.error.error_view import BugRequestError
from bugs.service.validator.validator import Validator


# ===========
# Обращение пользователя насчет багов
# ===========
class BugView(viewsets.ModelViewSet):
    serializer_class = BugSerializer
    queryset = Bug.objects.all()
    permission_classes = [permissions.AllowAny]
    error_adapter = BugRequestError()

    @action(detail=False, methods=['post'])
    def create_bug(self, request):
        validator = Validator(request=request, error_adapter=self.error_adapter)
        validator.is_not_content(need_data=['page', 'calling_error', 'description'])
        if validator.has_error:
            return validator.error

        new_bug = Bug.objects.create(
            page=request.data['page'],
            calling_error=request.data['calling_error'],
            description=request.data['description'],
        )
        new_bug.save()
        result = self.serializer_class(new_bug).data
        return Response(result, status=status.HTTP_200_OK)
