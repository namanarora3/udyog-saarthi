from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

from django.conf import settings

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **other_fields):
        if not email:
            raise (ValueError("Email not provided"))
        user = self.model(
            email=self.normalize_email(email),
            **other_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Issues(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_educator = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

    issue = models.ManyToManyField(Issues)

    USERNAME_FIELD = 'email'

    objects = UserManager()


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    educator = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issues, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    employer = models.ForeignKey(User, on_delete=models.CASCADE)

class Enrolledcourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    progress = models.IntegerField(default=0)



