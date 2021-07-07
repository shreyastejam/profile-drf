from registration.models import Registerextend
from rest_framework import serializers
from django.contrib.auth.models import User

# User Serializer
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')

# Register Serializer
class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registerextend
        fields = ('user','profile_photo','birth_date','age','gender','personal_description','personality_tags','prospective_university','sharing_preferences','course','city','flat_finder','admission','food_preferences','cooking_skills','source')
    
    def create(self, validated_data):
        Register = Registerextend.objects.create(user=validated_data['user'] ,profile_photo=validated_data['profile_photo'], birth_date=validated_data['birth_date'], age=validated_data['age'], gender=validated_data['gender'], personal_description=validated_data["personal_description"], personality_tags=validated_data["personality_tags"], sharing_preferences=validated_data["sharing_preferences"], city=validated_data["city"], course=validated_data["course"], flat_finder=validated_data["flat_finder"], admission=validated_data["admission"], food_preferences=validated_data["food_preferences"], cooking_skills=validated_data["cooking_skills"], source=validated_data["source"])
        return Register

