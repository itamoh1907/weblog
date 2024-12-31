from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
# many to one


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Article(models.Model):

    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    author= models.ForeignKey(User, on_delete=models.SET_DEFAULT,default='1')
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(default=timezone.now())
    is_published = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.title} - {self.body[:30]}"


class New(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.replace(' ','-')
        super(New,self).save(*args, **kwargs)

