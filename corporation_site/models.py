from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Event(models.Model):
    name = models.CharField(max_length=255)
    guests = models.IntegerField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='employee')
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='employees')
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
