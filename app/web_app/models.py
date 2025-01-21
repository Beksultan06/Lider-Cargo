from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
import random, string

def generate_user_id():
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    digits = ''.join(random.choices(string.digits, k=3))
    return letters + digits

def generate_code():
    return ''.join(random.choices(string.digits, k=10))

class User(AbstractUser):
    id_user = models.CharField(
        max_length=6,
        unique=True,
        default=generate_user_id,
        editable=False,
        verbose_name='Айди'
    )
    code = models.CharField(
        max_length=10,
        unique=True,
        default=generate_code,
        editable=False
    )
    full_name = models.CharField(max_length=255, verbose_name="ФИО")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    pickup_point = models.CharField(max_length=255, verbose_name="ПВЗ")
    address = models.TextField(verbose_name="Адрес")
    password = models.CharField(max_length=128, verbose_name="Пароль")
    password_confirmation = models.CharField(max_length=128, verbose_name="Подтверждение пароля")
    warehouse_address = models.TextField(verbose_name="Адрес склада")

    def save(self, *args, **kwargs):
        if self.password_confirmation and self.password != self.password_confirmation:
            raise ValueError("Пароли не совпадают.")
        super().save(*args, **kwargs)
        if not self.password.startswith("pbkdf2_"):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.id_user})"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"