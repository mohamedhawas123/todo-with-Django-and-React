from django.shortcuts import render
from .serializers import TodoSerilizers
from .models import Todo
from rest_framework import viewsets


class TotoIt(viewsets.ModelViewSet):
    serializer_class = TodoSerilizers
    queryset = Todo.objects.all()
