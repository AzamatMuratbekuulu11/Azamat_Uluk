from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import SkillViewSet, UserProfileViewSet, CategoryViewSet, ProjectViewSet, OfferViewSet, ReviewViewSet


router = SimpleRouter()
router.register(r'skill', SkillViewSet),
router.register(r'user', UserProfileViewSet),
router.register(r'category', CategoryViewSet),
router.register(r'project', ProjectViewSet),
router.register(r'offer', OfferViewSet),
router.register(r'review', ReviewViewSet),


urlpatterns = [
    path('', include(router.urls)),
]