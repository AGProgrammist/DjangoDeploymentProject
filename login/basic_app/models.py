from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    portfolia = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic')

    def __str__(self):
        return "Username: {}".format(self.user.username)
