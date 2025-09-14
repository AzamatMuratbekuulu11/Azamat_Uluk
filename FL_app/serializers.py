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


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class OfferSerializers(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

