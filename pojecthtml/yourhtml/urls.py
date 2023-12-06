from django.urls import path
from .views import product_list, view_user_input, view_success
from . import views

urlpatterns = [
    path('', product_list, name='product_list'),
    path('view_user_input/', view_user_input, name='view_user_input'),
    path('success/', view_success, name='success'),
    path('yourhtml/', views.view_index),
    path('contacts/', views.view_contacts),
]
