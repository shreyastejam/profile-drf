from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Registerextend(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo=models.ImageField(upload_to='images/')
    birth_date=models.DateTimeField(blank=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    personal_description=models.CharField(max_length=200)
    personality_tags=models.CharField(max_length=200)
    prospective_university=models.CharField(max_length=20)
    sharing_preferences=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    flat_finder=models.CharField(max_length=20)
    admission=models.CharField(max_length=20)
    food_preferences=models.CharField(max_length=20)
    cooking_skills=models.CharField(max_length=20)
    source=models.CharField(max_length=50)
    