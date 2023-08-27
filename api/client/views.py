from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Client, SocialNetwork
from .service.error.error_view import ClientError
from .service.validator.validator import Validator


class ClientView(viewsets.ModelViewSet):
    # serializer_class = BrandPartnerSerializer
    queryset = Client.objects.all()
    permission_classes = [permissions.AllowAny]
    error_adapter = ClientError()

    @action(detail=False, methods=['post'])
    def create_client(self, request):
        validator = Validator(request=request, error_adapter=self.error_adapter)
        validator.is_not_content(need_data=['username', 'number_phone', 'email', 'communication'])
        if validator.has_error:
            return validator.error

        clients_number_phone = self.queryset.filter(number_phone=request.data.get('number_phone'))
        clients_email = self.queryset.filter(email=request.data.get('email'))
        if len(clients_email) > 0:
            current_client = clients_email[0]
        elif len(clients_number_phone) > 0:
            current_client = clients_number_phone[0]
        else:
            social = SocialNetwork.objects.create()
            current_client = Client.objects.create(*request.data)
        #
        # auth = Profile.objects.get(user=self.request.user)
        # course = Course.objects.create(title=course_title, profile=auth)
        # course.save()
        # ProfileCourse.objects.create(course=course, profile=auth).save()
        return Response({
            # 'title': course.title,
            # 'path': course.path,
            'message': "Курс успешно создан",
        }, status=status.HTTP_200_OK)
