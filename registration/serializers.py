
from registration.models import Registerextend
from rest_framework import serializers
from django.contrib.auth.models import User

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registerextend
        fields = ('user','profile_photo','birth_date','age','gender','personal_description','personality_tags','prospective_university','sharing_preferences','course','city','flat_finder','admission','food_preferences','cooking_skills','source')




