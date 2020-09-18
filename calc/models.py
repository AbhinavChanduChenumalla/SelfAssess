from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, default=1,null=True, on_delete=models.SET_NULL)
    temperature = models.IntegerField()
    current_symptoms = models.CharField(max_length=100)
    previous_diseases = models.CharField(max_length=100)
    travel = models.BooleanField(default=False)
    social_distance = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

class Person(models.Model):
    username = models.CharField(max_length=12)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile_no = models.CharField(max_length=10)
    
