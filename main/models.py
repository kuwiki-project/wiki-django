from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from django.core.validators import MaxValueValidator, MinValueValidator


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(default='', max_length=10, blank=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(default='', max_length=60, blank=True)
    last_name = models.CharField(default='', max_length=60, blank=True)
    current_position = models.CharField(default='', max_length=64, blank=True)
    about = models.CharField(default='', max_length=255, blank=True)
    department = models.CharField(default='', max_length=128, blank=True)
    company = models.CharField(default='', max_length=128, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    icon_id = models.IntegerField(default=0)

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    def __str__(self):
        return self.email


class Course(models.Model):
    course_code = models.CharField(max_length=20, unique=True, blank=True, null=True)
    course_numbering = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    field = models.CharField(max_length=100, blank=True, null=True)


class Exam(models.Model):
    course_code = models.ForeignKey(Course,  db_column='course_code', to_field='course_code', on_delete=models.SET_NULL,  blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    field = models.CharField(max_length=100, blank=True, null=True)
    drive_id = models.CharField(max_length=1000, blank=True, null=True)
    drive_link = models.CharField(max_length=1000, blank=True, null=True)
    drive_link_tag = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    year = models.IntegerField(validators=[MinValueValidator(
        0), MaxValueValidator(3000)], null=True, blank=True)
    group_code = models.CharField(max_length=4, null=True, blank=True)
    code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    semester = models.CharField(max_length=10, null=True, blank=True)
    major = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    num_periods = models.IntegerField(null=True, blank=True)
    course_code = models.ForeignKey(Course,  db_column='course_code', to_field='course_code', on_delete=models.SET_NULL,  blank=True, null=True)
    course_numbering = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    lecture = models.ForeignKey(Lecture, db_column='code', to_field='code',
                                on_delete=models.SET_NULL,  blank=True, null=True)
    name = models.CharField(max_length=100, blank=False, null=False)


class Period(models.Model):
    lecture = models.ForeignKey(Lecture, db_column='code', to_field='code',
                                on_delete=models.SET_NULL,  blank=True, null=True)
    name = models.CharField(max_length=5, blank=False, null=False)
