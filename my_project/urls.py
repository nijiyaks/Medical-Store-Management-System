from django.contrib import admin
from django.urls import path,include
from greetings import views
urlpatterns = [
    path('',views.login_page,name='login'),
    path('products/',include('products.urls')),
    path('signup/',views.signup_page,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/', views.logout_view,name='logout'),

    
]



