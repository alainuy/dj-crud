from django.db import models
from django.utils import timezone

# Create your models here.

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    empid = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    joindate = models.DateField(default=timezone.now)

class Position(models.Model):
    title = models.CharField(max_length=50)
# Create a string representation of the posiition objects in list
    def __str__(self):
        return self.title
    
