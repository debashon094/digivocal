from django.urls import path
from django_facebook.urls import *
from django_facebook.auth_urls import *
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<login_id>', views.edit, name='edit'),
    path('delete/<login_id>', views.delete, name='delete'),
    path(r'^facebook/',views.fb,name='fb'),
    path(r'^accounts/',views.acc,name='acc'),
]