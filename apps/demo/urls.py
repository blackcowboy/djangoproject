from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('rsa_key', views.rsa_key),
    path('echarsView', views.echarsView),
    path('getFormData', views.getFormData),
]
