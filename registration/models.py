from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def get_upload_path(self, filename):
    return 'images/{0}/{1}'.format(self.user.id, filename)

class Registerextend(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    university_name = models.CharField(max_length=500, null=False, blank=False)
    university_image = models.CharField(max_length=10000, null=False, blank=True)
    university_latitude = models.FloatField()
    university_longitude = models.FloatField()
    profile_photo=models.ImageField(upload_to = get_upload_path,blank=True)
    birth_date=models.DateTimeField(blank=True,null=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    personal_description=models.CharField(max_length=200,blank=True,null=True)
    personality_tags=models.CharField(max_length=200, null=True)
    sharing_preferences=models.CharField(max_length=20, null=False)
    city=models.CharField(max_length=20, null=False)
    course=models.CharField(max_length=20, null=False)
    flat_finder=models.CharField(max_length=20, null=False)
    admission=models.CharField(max_length=20, null=False)
    food_preferences=models.CharField(max_length=20, null=False)
    cooking_skills=models.CharField(max_length=20)
    source=models.CharField(max_length=50, null=True)

