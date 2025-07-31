<<<<<<< HEAD
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
          path('dashboard/', views.dashboard_page, name='dashboard_page'),
]
=======

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.test_page, name='test_page'),
]
>>>>>>> 71420633b83e6aa3c44bd1a0fc304f9022e03c08
