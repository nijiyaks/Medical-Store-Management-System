from . import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
        path('create/', views.product_create, name='createproduct'),
        path('update/<int:pk>/',views.product_update,name='updateproduct'),
        path('delete/<int:pk>',views.product_delete,name='deleteproduct'),
        path('listing/',views.listing,name='page_list'),
        path('search/',views.search_products,name='search_products'),
         path('live-search/', views.live_search, name='live_search'),
    ]