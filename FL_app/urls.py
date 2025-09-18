from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import SkillViewSet, UserProfileListAPIView, UserProfileDetailAPIView, CategoryViewSet, ProjectListAPIView, ProjectDetailAPIView,  OfferViewSet, ReviewViewSet


router = SimpleRouter()
router.register(r'skill', SkillViewSet),
router.register(r'category', CategoryViewSet),
router.register(r'offer', OfferViewSet),
router.register(r'review', ReviewViewSet),


urlpatterns = [
    path('', include(router.urls)),
    path('project/', ProjectListAPIView.as_view(), name='project_list'),
    path('project/<int:pk>/', ProjectDetailAPIView.as_view(), name='project_detail'),
    path('accounts/', include('allauth.urls')),
    path('user/', UserProfileListAPIView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail')

]