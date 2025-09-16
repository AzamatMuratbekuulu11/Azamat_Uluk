from rest_framework import serializers
from .models import *


class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProjectListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'budget',]


class ProjectDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'budget', 'category', 'description', 'deadline', 'status', 'skills_required', 'client']


class OfferSerializers(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

