from django.shortcuts import render
from rest_framework import viewsets
from testreact.serializers import TodoSerializer
from testreact.models import Todo

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
