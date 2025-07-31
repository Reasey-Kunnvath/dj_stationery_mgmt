
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path ,include
=======
from django.urls import path, include
>>>>>>> 71420633b83e6aa3c44bd1a0fc304f9022e03c08
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('login/auth', views.auth_adm_login, name='auth_adm_login'),
<<<<<<< HEAD
    path("dashboard/", include('dashboard.dashboard_urls')),
=======
    
    path('dashboard/', include('dashboard.dashboard_urls')),
>>>>>>> 71420633b83e6aa3c44bd1a0fc304f9022e03c08
]
