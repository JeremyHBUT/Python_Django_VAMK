from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompanySerializer
from .models import Company


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
# Create your views here.
