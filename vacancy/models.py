from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):

    GENDER = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
    )

    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER)

    photo = models.ImageField(upload_to='users/')
    github = models.URLField()

    experience_years = models.PositiveIntegerField()
    stack = models.CharField(max_length=200)

    about = models.TextField()

    def __str__(self):
        return self.username