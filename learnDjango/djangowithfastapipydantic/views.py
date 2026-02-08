from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import Movies


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Movies.objects.filter(typ='action')
    serializer_class = MovieSerializer
