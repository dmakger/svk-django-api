from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from _service.mail.handler import MailHandler
from .models import Client, SocialNetwork, BusinessRequest, ServicesPackagePrice, ServicesPackage
from .serializers import ClientSerializer, BusinessRequestSerializer, ServicesPackageSerializer
from .service.error.error_view import ClientError, BusinessRequestError
from .service.validator.validator import Validator


# ===========
# Клиент
# ===========
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
            current_client = Client.objects.create(
                username=request.data['username'],
                number_phone=request.data['number_phone'],
                email=request.data['email'],
            )
            current_client.save()
        # SOCIAL NETWORK
        social_list = SocialNetwork.objects.filter(link=request.data.get('communication'))
        if social_list.exists():
            social = social_list.first()
        else:
            social = SocialNetwork.objects.create(link=request.data.get('communication'))
        current_client.communication.add(social)

        result = self.serializer_class(current_client).data
        return Response(result, status=status.HTTP_200_OK)


# ===========
# Бизнес запрос
# ===========
class BusinessRequestView(viewsets.ModelViewSet):
    serializer_class = BusinessRequestSerializer
    queryset = BusinessRequest.objects.all()
    permission_classes = [permissions.AllowAny]
    error_adapter = BusinessRequestError()

    @action(detail=False, methods=['post'])
    def create_business_request(self, request):
        validator = Validator(request=request, error_adapter=self.error_adapter)
        validator.is_not_content(need_data=['title', 'description', 'client_id', 'services_package'])
        if validator.has_error:
            return validator.error

        clients_id_list = Client.objects.filter(id=request.data['client_id'])
        services_package_list = ServicesPackagePrice.objects.filter(id__in=request.data['services_package'])
        if len(clients_id_list) == 0:
            return self.error_adapter.is_not_found_curr(['client_id'])
        if len(services_package_list) != len(request.data['services_package']):
            return self.error_adapter.is_not_found_curr([f'services_package'])
        business_request_list = self.queryset.filter(client=clients_id_list[0], title=request.data['title'])
        if len(business_request_list) > 0:
            current_business_request = business_request_list[0]
            package_all = current_business_request.services_package_price.all()
            for services_package in services_package_list:
                if services_package not in package_all:
                    current_business_request.services_package_price.add(services_package)
            current_business_request.save()
        else:
            current_business_request = BusinessRequest.objects.create(
                title=request.data['title'],
                description=request.data['description'],
                client=clients_id_list[0],
            )
            current_business_request.services_package_price.set(services_package_list)
            current_business_request.save()
        result = self.serializer_class(current_business_request).data
        mail = MailHandler()
        mail.send_auto_write_to_application(recipients=[clients_id_list[0].email])
        mail.send_new_application(content=result, new_subject=f": {clients_id_list[0].email}")
        return Response(result, status=status.HTTP_200_OK)


# ===========
# Бизнес запрос
# ===========
class ServicesPackageView(viewsets.ModelViewSet):
    serializer_class = ServicesPackageSerializer
    queryset = ServicesPackage.objects.all()
    permission_classes = [permissions.AllowAny]

    @action(detail=False, methods=['post'])
    def get_services_package(self, request):
        result = self.serializer_class(self.queryset, many=True).data
        return Response(result, status=status.HTTP_200_OK)

