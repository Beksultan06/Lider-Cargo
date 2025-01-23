from django.urls import path
from .views import login, register, index, redirect_to_qr_path

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name='login'),
    path("index/", index, name='index'),
    path('redirect/<path:qr_path>/', redirect_to_qr_path, name='redirect_to_qr_path'),
]
