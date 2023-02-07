from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import PlaceSerializer
from django.http import JsonResponse
from .models import Place
from django_filters.rest_framework import DjangoFilterBackend


class PlaceList(generics.ListAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fileds = ['name', 'description']


# Create your views here.
