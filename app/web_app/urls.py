from django.urls import path
from .views import login, register, index

urlpatterns = [
    path("register/", register, name="register"),
    path("login", login, name='login'),
    path("index", index, name='index'),
]
