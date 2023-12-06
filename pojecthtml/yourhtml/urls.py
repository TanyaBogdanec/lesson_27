from django.urls import path
from .views import account_list, view_user_input, view_success
from . import views

urlpatterns = [
    path('', account_list, name='account_list'),
    path('view_user_input/', view_user_input, name='view_user_input'),
    path('success/', view_success, name='success'),
    path('main/', views.view_index),
    path('contacts/', views.view_contacts),
]
