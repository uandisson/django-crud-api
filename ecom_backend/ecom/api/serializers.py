from django.contrib.auth.models import User, Group

from rest_framework import serializers 

from ecom.models import Category, Product
#GraphQL
from django_restql.mixins import DynamicFieldsMixin

class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProductSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', )


    
