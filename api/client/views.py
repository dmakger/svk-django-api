from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Client, SocialNetwork
from .serializers import ClientSerializer
from .service.error.error_view import ClientError
from .service.validator.validator import Validator


class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
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
            social_list = SocialNetwork.objects.filter(link=request.data.get('communication'))
            if len(social_list) > 0:
                social = social_list
            else:
                social = SocialNetwork.objects.create(link=request.data.get('communication'))
            current_client = Client.objects.create(
                username=request.data['username'],
                number_phone=request.data['number_phone'],
                email=request.data['email'],
            )
            current_client.communication.set(social),
            current_client.save()
        result = self.serializer_class(current_client).data
        return Response(result, status=status.HTTP_200_OK)
