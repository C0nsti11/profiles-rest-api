from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status

# Create your views here.

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
        
    @property
    def allowed_methods(self):
        allowed_methods = super().allowed_methods
        allowed_methods.remove('OPTIONS')
        return allowed_methods