from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login as auth_login
from .models import User
from aiogram import Bot
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.environ.get("token"))

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect("index")  # Перенаправление на главную страницу, если пользователь уже залогинен

    chat_id = request.GET.get("chat_id")  # Получаем chat_id из параметров запроса

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        pickup_point = request.POST.get("pickup_point")
        address = request.POST.get("address")
        warehouse_address = request.POST.get("warehouse_address")
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")

        if password != password_confirmation:
            messages.error(request, "Пароли не совпадают!")
            return render(request, "register.html", {"chat_id": chat_id})

        if User.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Пользователь с таким номером телефона уже существует!")
            return render(request, "register.html", {"chat_id": chat_id})

        try:
            user = User.objects.create_user(
                username=phone_number,
                password=password,
                full_name=full_name,
                phone_number=phone_number,
                pickup_point=pickup_point,
                address=address,
                warehouse_address=warehouse_address,
                chat_id=chat_id,
            )
            # Логиним пользователя сразу после регистрации
            auth_login(request, user)
            messages.success(request, "Регистрация прошла успешно! Вы вошли в систему.")
            return redirect("index")
        except IntegrityError:
            messages.error(request, "Ошибка: Пользователь с таким именем или номером телефона уже существует!")
        except Exception as e:
            messages.error(request, f"Ошибка при регистрации: {e}")

    return render(request, "register.html", {"chat_id": chat_id})


def login(request):
    if request.method == "POST":
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")

        user = authenticate(username=phone_number, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Вы успешно вошли в систему!")
            return redirect("index")
        else:
            messages.error(request, "Неверный номер телефона или пароль!")

    return render(request, "login.html")