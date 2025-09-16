from rest_framework import viewsets, generics
from .models import Skill, UserProfile, Category, Project, Offer, Review
from .serializers import SkillSerializers, UserProfileSerializers, CategorySerializers, ProjectListSerializers, ProjectDetailSerializers, OfferSerializers, ReviewSerializers
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProjectFilter
from rest_framework.filters import SearchFilter


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializers


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializers
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProjectFilter
    search_fields = ['title', 'category']


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetailSerializers


class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializers


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers