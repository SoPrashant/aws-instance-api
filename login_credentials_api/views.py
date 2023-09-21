from django.shortcuts import render
from rest_framework import viewsets
from .models import CloudLogin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import CloudLoginSerializer

class CloudLoginViewSet(generics.CreateAPIView):
    queryset = CloudLogin.objects.all()
    serializer_class = CloudLoginSerializer
