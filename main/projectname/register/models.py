from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"

    role = models.CharField(max_length=50, choices=Role.choices)





