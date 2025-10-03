from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TurnViewSet

router = DefaultRouter()
router.register(r'turns', TurnViewSet, basename='turn')

urlpatterns = [
    path('', include(router.urls)),
]
