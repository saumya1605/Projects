from django.shortcuts import render
from rest_framework import generics
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.


class ListTodo(generics.ListAPIView):  # READ
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodo(generics.RetrieveUpdateAPIView):  # UPDATE
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class CreateTodo(generics.CreateAPIView):  # CREATE
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DeleteTodo(generics.DestroyAPIView):  # DELETE
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
