from django.db import models
from django.contrib.auth.models import BaseUserManager, \
    AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, name, password=None, **kwargs):
        if not email:
            raise ValueError('email field is mandatory!')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            **kwargs
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None):

        user = self.create_user(email=email,
                                name=name,
                                password=password)
        user.is_superuser = True
        user.save(using=self._db)

        return user


class MyUser(AbstractBaseUser):
    # custome user model - accepts email instead of username
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # date_of_birth = models.DateField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):

        return self.email
