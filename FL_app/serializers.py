from rest_framework import serializers
from .models import *


class SkillSerializers(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class UserProfileListSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'avatar']


class UserProfileDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'avatar', 'phone_number', 'bio', 'role', 'skills', 'social_links']


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

