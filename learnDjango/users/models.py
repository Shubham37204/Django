from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE) #connect profile to user
    image= models.ImageField(default="profilePic.jpg",upload_to='profile')
    location= models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    
    