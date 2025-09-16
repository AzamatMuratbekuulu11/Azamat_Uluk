from .models import Skill, UserProfile, Project
from modeltranslation.translator import TranslationOptions,register


@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('skill_name', )


@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('bio', )


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )