from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from users.models.managers import UserManager


class User(AbstractUser):
    username = models.CharField("Логин", max_length=30, unique=True, null=True, blank=True)
    email = models.EmailField("Электронная почта", max_length=254, unique=True, blank=True)
    first_name = models.CharField("Имя", max_length=30, blank=True)
    last_name = models.CharField("Фамилия", max_length=30, blank=True)
    phone_number = PhoneNumberField("Телефон", unique=True, null=True, blank=True)
    photo = models.ImageField(
        "Фотография пользователя", upload_to="users", blank=True, null=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    objects = UserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.full_name}({self.pk})"
