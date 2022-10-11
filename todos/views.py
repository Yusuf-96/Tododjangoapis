from django.shortcuts import render
from .models import Todo
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status
from .serializers import TodoSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


# Create your views here.

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


   

class ListTodo(APIView):
   def get(self, request, *args, **kwargs):
      
      todos = Todo.objects.all().order_by('-updated')
      serializer = TodoSerializer(todos, many= True)
      return Response(serializer.data)
   
   def post(self, request, *args, **kwargs):
    
      if request.method == 'POST':
         data = request.data
         serializer = TodoSerializer(data=data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
      return Response("Todo Created Successefully")

class DetailTodo(APIView):
   def get(self, request, *args, pk, **kwargs):
      
      if request.method =='GET':
         todo = Todo.objects.get(id=pk)
         serializer = TodoSerializer(todo)
         return Response(serializer.data)

   def put(self, request, *args, pk, **kwars):
    
      if request.method =='PUT':
         todos = Todo.objects.get(id=pk)
         data = request.data
         serializer = TodoSerializer(instance=todos, data=data)

         if serializer.is_valid():
            serializer.save()
         return Response(serializer.data)
      return Response('Todo updated')

   def delete(self, request, *args, pk, **kwargs):
      
      if request.method =='DELETE':
         todos = Todo.objects.get(id=pk)
         todos.delete()
         return Response('Todo Deleted')
     

             