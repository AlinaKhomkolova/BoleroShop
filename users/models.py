from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from config.settings import NULLABLE


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=30,
        blank=False
    )
    slug = models.SlugField(
        verbose_name='Slug',
        max_length=30,
        unique=True
    )
    date_of_birth = models.DateField(
        verbose_name='Дата рождения', **NULLABLE
    )
    is_active = models.BooleanField(
        verbose_name='Активирован',
        default=True
    )
    is_staff = models.BooleanField(
        verbose_name='Статус администратора',
        default=False
    )
    created = models.DateTimeField(
        verbose_name='Дата регистрации',
        auto_now_add=True
    )
    updated = models.DateTimeField(
        verbose_name='Последнее обновление',
        auto_now=True
    )

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['-created']

        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
