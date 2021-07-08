
# Register API
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers, viewsets,status
from .serializers import AuthSerializer, RegisterSerializer
from .models import Registerextend
from rest_framework.response import Response
from roombae.settings import MEDIA_ROOT
from django.core.files.storage import FileSystemStorage

# Create your views here.


class RegisterView(viewsets.ModelViewSet):
    serializer_class = RegisterSerializer
    queryset = Registerextend.objects.all()
    def create(self, request):

        if Registerextend.objects.filter(user=request.data['user']).exists():
            raise serializers.ValidationError(
                {"success": False, "response": "profile already added"})
        if request.data['gender'] == "" or not(request.data['gender'] == 'Male' or request.data['gender'] == 'Female' or request.data['gender'] == 'Non-Binary'):
            raise serializers.ValidationError(
                {"success": False, "reponse": "Gender is a compulsory field and enter a valid gender"})
        if request.data["city"] == "":
            raise serializers.ValidationError(
                {"success": False, "reponse": "City is a compulsory field"})
        if request.data["admission"] == "":
            raise serializers.ValidationError({
                "success": False, "response": "Admission is a compulsory field"
            })
        if request.data["course"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Course is a compulsory field"})
        if request.data["flat_finder"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Flat finding details are essential"})
        if request.data["sharing_preferences"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Sharing Preferences are essential"})
        if request.data["food_preferences"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "Food prefernce is an essential field"})
        if request.data["cooking_skills"] == "":
            raise serializers.ValidationError(
                {"success": False, "response": "cooking skills are essential"})

        user=User.objects.get(id=request.data['user'])

        register = Registerextend.objects.create(
            user=user,
            birth_date=request.data['birth_date'],
            age=request.data['age'],
            gender=request.data['gender'],
            personal_description=request.data["personal_description"],
            city=request.data["city"],
            course=request.data["course"],
            admission=request.data["admission"],
            flat_finder=request.data["flat_finder"],
            sharing_preferences=request.data["sharing_preferences"],
            food_preferences=request.data["food_preferences"],
            cooking_skills=request.data["cooking_skills"],
            personality_tags=request.data["personality_tags"],
            prospective_university=request.data.get("university_name","university_image","university_latitude","university_longitude")
        )
        image = request.data.get('profile_photo')
        if image:
            fileStorage = FileSystemStorage(location=MEDIA_ROOT/f'images/{user.id}')
            image_file = fileStorage.save(image.name, image)
            print(image_file)
            register.profile_photo = f'images/{user.id}/' + str(image_file)
            register.save()
        data = {
            'user': register.user,
            'profile_photo': register.profile_photo.url,
            'birth_day': register.birth_date,
            'age': register.age,
            'gender': register.gender,
            'personal_description': register.personal_description,
            'personality_tags': register.personality_tags.split(","),
            'sharing_preferences': register.sharing_preferences,
            'city': register.city,
            'course': register.course,
            'flat_finder': register.flat_finder,
            'admission': register.admission,
            'food_preferences': register.food_preferences,
            'cooking_skills': register.cooking_skills,
            'source': register.source,
            "prospective_university": {
                "name": register.university_name,
                "photo": register.university_image,
                "latitude": register.university_latitude,
                "longitude": register.university_longitude,
            }
        }
        return Response(data, status=status.HTTP_201_CREATED)


# class register(viewsets.ViewSet):
#     def create(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

        
class UserView(viewsets.ModelViewSet):
    serializer_class = AuthSerializer
    queryset = User.objects.all()


class user(viewsets.ViewSet):
    def create(self, request):
        serializer = AuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

