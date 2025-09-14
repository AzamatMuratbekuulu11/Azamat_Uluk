from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Skill(models.Model):
    skill_name = models.CharField(max_length=32, unique=True)


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=True)
    ROLE_CHOICES = (
        ('client', 'client '),
        ('freelancer', 'freelancer'),
    )
    role = models.CharField(choices=ROLE_CHOICES, default='freelancer', max_length=32)
    create_date = models.DateTimeField(auto_now_add=True)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='avatar_photo/')
    skills = models.ManyToManyField(Skill, blank=True)
    social_links = models.JSONField(default=list, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


# class Social_Network(models.Model):
#     name = models.URLField()
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Project(models.Model):
    SATUS_CHOICES = (
        ('open', 'open'),
        ('in_progress', 'in_progress'),
        ('completed', 'completed'),
        ('cancelled', 'cancelled'),
    )
    title = models.CharField(max_length=32)
    description = models.TextField()
    budget = models.IntegerField()
    deadline = models.DateField()
    status = models.CharField(choices=SATUS_CHOICES, default='open', max_length=32)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    skills_required = models.ManyToManyField(Skill, blank=True)
    client = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.budget}'


class Offer(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    freelancer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    proposed_budget = models.IntegerField()
    proposed_deadline = models.DateField()
    date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_written')
    target = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_received')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
