from django.db import models
from django.contrib.auth.models import User
from datetime import date

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    dob = models.DateField(max_length=8, default=date.today())
    gender = models.CharField(max_length=7, choices=GENDER_CHOICES, default='Male')
    def __str__(self):
      return self.user.username
