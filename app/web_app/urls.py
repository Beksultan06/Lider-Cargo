from django.urls import path
from .views import register_cklient, index, redirect_to_qr_path, register_manager, register

urlpatterns = [
    path("register/", register, name="register"),
    path("cklient/", register_cklient, name="register_cklient"),
    path('manager/', register_manager, name='register_manager'),
    path("index/", index, name='index'),
    path('redirect/<path:qr_path>/', redirect_to_qr_path, name='redirect_to_qr_path'),
]