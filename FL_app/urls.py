from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import SkillViewSet, UserProfileViewSet, CategoryViewSet, ProjectListAPIView, ProjectDetailAPIView,  OfferViewSet, ReviewViewSet


router = SimpleRouter()
router.register(r'skill', SkillViewSet),
router.register(r'user', UserProfileViewSet),
router.register(r'category', CategoryViewSet),
# router.register(r'project', ProjectViewSet),
router.register(r'offer', OfferViewSet),
router.register(r'review', ReviewViewSet),


urlpatterns = [
    path('', include(router.urls)),
    path('project/', ProjectListAPIView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailAPIView.as_view(), name='project_detail'),

]