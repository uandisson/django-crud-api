from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from ecom.models import Category, Product

from .permissions import IsOwnerOrReadOnly, IsAuthenticated
from .serializers import ProductSerializer, CategorySerializer
from .pagination import CustomPagination


class getDeleteUpdateProduct(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            content = {
                'status': 'Not found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return product

    # Get a product
    def get(self, request, pk):

        product = self.get_queryset(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a product
    def put(self, request, pk):
        
        product = self.get_queryset(pk)

        if(request.user == product.creator): # If creator is who makes request
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a product
    def delete(self, request, pk):

        product = self.get_queryset(pk)

        if(request.user == product.creator): # If creator is who makes request
            product.delete()
            content = {
                'status': 'No content'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class getPostProducts(ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       products = Product.objects.all()
       return products

    # Get all products
    def get(self, request):
        products = self.get_queryset()
        paginate_queryset = self.paginate_queryset(products)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new product
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Category

class getDeleteUpdateCategory(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self, pk):
        try:
            category = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            content = {
                'status': 'Not found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)
        return category

    # Get a category
    def get(self, request, pk):

        category = self.get_queryset(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Update a category
    def put(self, request, pk):
        
        category = self.get_queryset(pk)

        if(request.user == category.creator):
            serializer = CategorySerializer(category, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    # Delete a category
    def delete(self, request, pk):

        category = self.get_queryset(pk)

        if(request.user == category.creator):
            category.delete()
            content = {
                'status': 'No content'
            }
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        else:
            content = {
                'status': 'UNAUTHORIZED'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)
   

class getPostCategories(ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    
    def get_queryset(self):
       categories = Category.objects.all()
       return categories

    # Get all categories
    def get(self, request):
        categories = self.get_queryset()
        paginate_queryset = self.paginate_queryset(categories)
        serializer = self.serializer_class(paginate_queryset, many=True)
        return self.get_paginated_response(serializer.data)

    # Create a new category
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(creator=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

