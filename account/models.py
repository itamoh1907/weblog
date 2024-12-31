from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fathername = models.CharField(max_length=100)
    nat_code = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics',null=True, blank=True)



    def __str__(self):
        return self.user.username
