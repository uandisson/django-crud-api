"""ecom_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import RegisterView, CustomLoginView

from ecom.api import viewsets
 
schema_view = get_schema_view(
   openapi.Info(
      title="E-comerce Rest API Document",
      default_version='v1',
      description="E-comerce Rest API Document Description",
      terms_of_service="https://www.localhost:8080/policies/terms/",
      contact=openapi.Contact(email="user@ecom.local"),
      license=openapi.License(name="License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

API_VERSION = 'api/v1/'

#other way with graphql
#router = routers.DefaultRouter()
#router.register(API_VERSION + 'products', viewsets.ProductViewSet, basename='Products')
#router.register(API_VERSION + 'categories', viewsets.CategorySerializer, basename='Categories')

urlpatterns = [
    path('admin/', admin.site.urls),
    
    url(API_VERSION, include('ecom.urls')),
    
    #url('', include(router.urls)), #other way

    url(API_VERSION + 'swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(API_VERSION + 'swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(API_VERSION + 'redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path(API_VERSION + 'login/', CustomLoginView.as_view()),
    path(API_VERSION + 'registration/', RegisterView.as_view()),
    path(API_VERSION + 'rest-auth/', include('rest_auth.urls')),
    
    #other way
    #path(API_VERSION + 'token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path(API_VERSION + 'token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]