from django.shortcuts import render
from django.http.response import JsonResponse
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated 

from ecom.api.serializers import UserSerializer, CategorySerializer, ProductSerializer
from ecom.models import Category, Product


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    queryset = Product.objects.all()

    def get_serializer_class(self):
        
        actions = [
            'create',
            'update',
            'partial_update'
        ]
        
        if self.action in actions:
            return self.serializer_class #can specify some action
        
        return self.serializer_class #can specify some action
        

class CategorySerializer(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
