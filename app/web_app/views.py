from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth import authenticate, login as auth_login
from .models import User, Pvz
from aiogram import Bot
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(token=os.environ.get("token"))

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect("index")

    chat_id = request.GET.get("chat_id")

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        pickup_point_name = request.POST.get("pickup_point")  # Получаем имя ПВЗ как строку
        address = request.POST.get("address")
        warehouse_address = request.POST.get("warehouse_address")
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")

        # Проверка совпадения паролей
        if password != password_confirmation:
            messages.error(request, "Пароли не совпадают!")
            return render(request, "register.html", {"chat_id": chat_id})

        # Проверка существующего номера телефона
        if User.objects.filter(phone_number=phone_number).exists():
            messages.error(request, "Пользователь с таким номером телефона уже существует!")
            return render(request, "register.html", {"chat_id": chat_id})

        # Получение или создание объекта Pvz
        try:
            pickup_point = Pvz.objects.get(city=pickup_point_name)  # Проверяем существующий ПВЗ
        except Pvz.DoesNotExist:
            pickup_point = Pvz.objects.create(city=pickup_point_name)  # Создаем новый ПВЗ, если его нет

        try:
            # Создаем пользователя
            user = User.objects.create_user(
                username=phone_number,
                password=password,
                full_name=full_name,
                phone_number=phone_number,
                pickup_point=pickup_point,  # Передаем объект Pvz
                address=address,
                warehouse_address=warehouse_address,
                chat_id=chat_id,
            )
            # Авторизуем пользователя
            auth_login(request, user)
            messages.success(request, "Регистрация прошла успешно! Вы вошли в систему.")
            return redirect("index")
        except IntegrityError:
            messages.error(request, "Ошибка: Пользователь с таким именем или номером телефона уже существует!")
        except Exception as e:
            messages.error(request, f"Ошибка при регистрации: {e}")

    return render(request, "register.html", {"chat_id": chat_id})

def redirect_to_qr_path(request, qr_path):
    """
    Обрабатывает ссылку из QR-кода и перенаправляет пользователя.
    """
    if qr_path.startswith("http://") or qr_path.startswith("https://"):
        return redirect(qr_path)
    else:
        return HttpResponse(f"Путь из QR-кода: {qr_path}")