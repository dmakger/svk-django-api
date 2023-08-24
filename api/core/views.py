from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import BrandPartner


# ===========
# Партнеры бренда
# ===========
class BrandPartnerView(viewsets.ModelViewSet):
    # serializer_class = MovieSerializer
    queryset = BrandPartner.objects.all()
    permission_classes = [permissions.AllowAny]

    # error_helper = BrandPartnerError()

    @action(methods=['get'], detail=False)
    def get_brand_partners(self, request):
        return Response(
            self.serializer_class(self.queryset).data,
            status=status.HTTP_200_OK,
        )
