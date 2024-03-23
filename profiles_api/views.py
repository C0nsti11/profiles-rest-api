from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status, viewsets
# from rest_framework.viewsets import ModelViewSet
# from profiles_api import permissions
# Create your views here.

methods = ['get', 'head', 'post']

class HelloApiView(APIView):
    """Test Api View"""
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """Returns a list of APIView featues"""
        
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete',
            'Is similar to a traditional Django View.',
            'Gives you the most control over your application logic',
            'Is  mapped manually to URLs',
        ]
        
        return Response( {'message': 'Hello!', 'an_apiview':an_apiview})
    
    def post(self, request):
        """Creat a hello message wiith our name"""
        
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello {}'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    http_method_names = methods     
    # @property
    # def allowed_methods(self):
    #     allowed_methods = super().allowed_methods
    #     allowed_methods.remove('OPTIONS')
    #     return allowed_methods
    
    
class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""
    
    # http_method_names = methods
    serializer_class = serializers.HelloSerializer
    # permission_classes = [DisableDangerousMethods]
    
    def list(self, request):
        """Return a hello message"""
        
        a_viewset = [
            'Uses Action (list, create, retrieve, update, partial_update)',
            'Automatically maps to urls using routers',
            'Provides more functionality using less code',
        ]
        
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """
        Create a new hello message
        """
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = "Hello {}".format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )
    
    def retrive(self, request, pk=None):
        """
        Handle getting an object by iits ID
        """
        return Response({'http_method':'GET'})
    
    def update(self, request, pk=None):
        """
        Handle updating an object
        """
        return Response({'http_method':'PUT'})
    
    def partial_update(self, request, pk=None):
        """
        Handle partial updating an object
        """
        return Response({'http_method':'PATCH'})
    
    def destroy(self, request, pk=None):
        """
        Handle deleting an object
        """
        return Response({'http_method':'DELETE'})