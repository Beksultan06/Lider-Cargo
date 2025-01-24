from django.urls import path
from .views import register, index, redirect_to_qr_path

urlpatterns = [
    path("register/", register, name="register"),
    path("index/", index, name='index'),
    path('redirect/<path:qr_path>/', redirect_to_qr_path, name='redirect_to_qr_path'),
]
