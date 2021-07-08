# from django.shortcuts import render

# # Create your views here.
# from rest_framework import generics, permissions
# from rest_framework.fields import ImageField
# from rest_framework.response import Response
# from knox.models import AuthToken
# from .serializers import UserSerializer, RegisterSerializer
# from rest_framework import viewsets

# Register API
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers, viewsets,status
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from .serializers import AuthSerializer, RegisterSerializer
from .models import Registerextend
from rest_framework.response import Response
# Create your views here.


class RegisterView(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = Registerextend.objects.all()


class register(viewsets.ViewSet):
    def create(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def create(self, validated_data):

        if Registerextend.objects.filter(user=validated_data['user']).exists():
            raise serializers.ValidationError(
                {"success": False, "response": "profile already added"})
        if validated_data['gender'] == "" or not(validated_data['gender'] == 'Male' or validated_data['gender'] == 'Female' or validated_data['gender'] == 'Non-Binary'):
            raise serializers.ValidationError(
                {"success": False, "reponse": "Gender is a compulsory field and enter a valid gender"})
        if validated_data["city"] == "":
            raise serializers.ValidationError(
                {"success": False, "reponse": "City is a compulsory field"})
        if validated_data["admission"] == "":
            raise serializers.ValidationError({
                "success": False, "response": "Admission is a compulsory field"
            })
        if validated_data["course"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Course is a compulsory field"})
        if validated_data["flat_finder"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Flat finding details are essential"})
        if validated_data["sharing_preferences"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Sharing Preferences are essential"})
        if validated_data["food_preferences"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Food prefernce is an essential field"})
        if validated_data["cooking_skills"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "cooking skills are essential"})
        if validated_data["university"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "university is an essential field and can't be null"})

        profile = Registerextend.objects.create(
            birth_date=validated_data['birth_date'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            personal_description=validated_data["personal_description"],
            city=validated_data["city"],
            course=validated_data["course"],
            admission=validated_data["admission"],
            flat_finder=validated_data["flat_finder"],
            sharing_preferences=validated_data["sharing_preferences"],
            food_preferences=validated_data["food_preferences"],
            cooking_skills=validated_data["cooking_skills"],
            personality=validated_data["personality"],
            university=validated_data["university"]
        )
        return profile    

class UserView(viewsets.ModelViewSet):
    serializer_class = AuthSerializer
    queryset = User.objects.all()


class user(viewsets.ViewSet):
    def create(self, request):
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

