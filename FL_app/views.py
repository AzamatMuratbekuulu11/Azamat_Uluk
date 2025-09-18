from rest_framework import viewsets, generics, permissions
from .models import Skill, UserProfile, Category, Project, Offer, Review
from .serializers import SkillSerializers, UserProfileListSerializers, UserProfileDetailSerializers, CategorySerializers, ProjectListSerializers, ProjectDetailSerializers, OfferSerializers, ReviewSerializers
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProjectFilter
from rest_framework.filters import SearchFilter


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializers


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializers


class UserProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProjectListAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProjectFilter
    search_fields = ['title', 'category']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializers
    permission_classes = [permissions.IsAuthenticated]


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializers


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers