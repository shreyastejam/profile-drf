from django.db import models
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

# Create your models here.

def get_upload_path(self, filename):
    return 'images/{0}/{1}'.format(self.user.id, filename)

class Registerextend(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo=models.ImageField(upload_to = get_upload_path,blank=True)
    birth_date=models.DateTimeField(blank=True,null=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    personal_description=models.CharField(max_length=200,blank=True,null=True)
    personality_tags=models.CharField(max_length=200, null=True)
    prospective_university=models.CharField(max_length=20, null=False)
    sharing_preferences=models.CharField(max_length=20, null=False)
    city=models.CharField(max_length=20, null=False)
    course=models.CharField(max_length=20, null=False)
    flat_finder=models.CharField(max_length=20, null=False)
    admission=models.CharField(max_length=20, null=False)
    food_preferences=models.CharField(max_length=20, null=False)
    cooking_skills=models.CharField(max_length=20)
    source=models.CharField(max_length=50, null=True)
    
    # def clean(self):
    #     if User.objects.filter(user_id=self.user_id.id).exists():
    #         raise ValidationError(
    #             "User already exists")
    #     if self.gender == "":
    #         raise ValidationError(
    #             "Gender is a compulsory to fill")
    #     if self.city == "":
    #         raise ValidationError(
    #              "City is a compulsory to fill")
    #     if self.admission == "":
    #         raise ValidationError(
    #             "Admission is a compulsory to fill")
    #     if self.course == "":
    #         raise  ValidationError(
    #             "Course is a compulsory to fill")
    #     if self.prospective_university == "":
    #         raise  ValidationError(
    #             "University is a compulsory to fill")
    #     if self.flat_finder == "":
    #         raise  ValidationError(
    #             "Flat finding details is required to fill")
    #     if self.sharing_preferences == "":
    #         raise ValidationError(
    #         "Sharing Preferences are required to fill")
    #     if self.food_preferences == "":
    #         raise  ValidationError(
    #             "Food prefernce is required")
    #     if self.cooking_skills == "":
    #         raise ValidationError(
    #             "cooking skills are essential")