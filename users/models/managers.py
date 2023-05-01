from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email=None, phone_number=None, password=None, **extra_fields):
        if not email:
            raise ValueError("У пользователя должна быть электронная почта")

        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.phone_number = phone_number
        user.save(using=self._db)
        return user

    def create_user(self, email, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, phone_number, password, **extra_fields)

    def create_superuser(self, email, phone_number, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self._create_user(email, phone_number,  password, **extra_fields)
