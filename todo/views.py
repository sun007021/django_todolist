from rest_framework import viewsets
from .serializer import TodolistSerializer
from .models import Todolist


class TodolistViewSet(viewsets.ModelViewSet):
    queryset = Todolist.objects.all()
    serializer_class = TodolistSerializer
