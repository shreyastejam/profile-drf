from django.conf import settings
from django.conf.urls.static import static
from .views import RegisterView, UserView
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'Register', RegisterView, 'Register')
router.register(r'User', UserView, 'User')

urlpatterns = [
   path('api/', include(router.urls)),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
