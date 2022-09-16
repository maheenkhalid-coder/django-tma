from django.shortcuts import render
# viewsets class provides the implementation for CRUD operations by default, what we had to do was specify the serializer class and the query set.
from rest_framework import viewsets          # add this
from .serializers import TodoSerializer      # add this
from .models import Todo                     # add this
from rest_framework.response import Response
from rest_framework import status

from rest_framework.generics import GenericAPIView

class TodoApi(GenericAPIView):                
    serializer_class = TodoSerializer         
# This method for get the info
    def get(self, request, pk = None, format=None):
        id=pk
        if id is not None:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data)

        todo = Todo.objects.all()
        serializer = TodoSerializer(todo, many=True)
        return Response(serializer.data)

    # This method for enter the info
    def post(self, request, format=None):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data entered'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        # This method for update the info
    def put(self, request, pk, format=None):
        id = pk
        todo = Todo.objects.get(pk=id)
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ({'msg': 'Success data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # This method for partial update the info
    def patch(self, request, pk, format=None):
        id = pk
        todo = Todo.objects.get(pk=id)
        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response ({'msg': 'partial data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # This method for delete the info
    def delete(self, request, pk, format=None):
        id = pk
        todo = Todo.objects.get(pk=id)
        todo.delete()
        return Response ({'msg': 'data deleted'})
