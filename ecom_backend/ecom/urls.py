from django.urls import include, path, re_path
from ecom.api import views


urlpatterns = [
    re_path(r'^products/(?P<pk>[0-9]+)$',
        views.getDeleteUpdateProduct.as_view(),
        name='getDeleteUpdateProduct'
    ),
    
    path('products/',
        views.getPostProducts.as_view(),
        name='getPostProducts'
    ),

    re_path(r'^categories/(?P<pk>[0-9]+)$',
        views.getDeleteUpdateCategory.as_view(),
        name='getDeleteUpdateCategory'
    ),

    path('categories/',
        views.getPostCategories.as_view(),
        name='getPostCategories'
    )
]