from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.hashers import make_password


class ProfileManager(BaseUserManager):
    def create_user(self, username, user_contact, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        if not email:
            raise ValueError('The Email field must be set')
        hashed_pwd = make_password(password, salt=None)
        user = self.model(
            username=username,
            user_contact=user_contact,
            password=hashed_pwd,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, username, user_contact, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not email:
            raise ValueError('The Email field must be set')
        user = self.create_user(
            username=username,
            user_contact=user_contact,
            email=email,
            password=password,
            **extra_fields
        )
        user.save(using=self._db)
        return user


class Profile(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    user_contact = models.CharField(max_length=20, unique=True)
    email = models.CharField(max_length=50, unique=True, default='')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='profile_set',  # Custom related_name
        related_query_name='profile'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='profile_set',  # Custom related_name
        related_query_name='profile'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_contact']

    objects = ProfileManager()

    def __str__(self):
        return self.email
