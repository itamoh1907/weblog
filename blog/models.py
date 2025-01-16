from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.utils import timezone
# many to one
from django.urls import reverse
from django.utils.text import slugify
class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager,self).get_queryset().filter(is_published=True)





class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class Article(models.Model):

    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category,related_name='articles')
    author= models.ForeignKey(User, on_delete=models.SET_DEFAULT,default='1')
    body = models.TextField()
    image = models.ImageField(upload_to="images/articles")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(default=timezone.now())
    is_published = models.BooleanField(default=True)
    published = models.BooleanField(default=True)
    # objects = models.Manager()
    # articles = models.Manager()
    slug = models.SlugField(null=True,blank=True,unique=True)
    objects = models.Manager()
    custom_manager = ArticleManager()

    def get_absolute_url(self):
        return reverse('blog:article_details',args = [self.slug])

    def save(self,force_insert=False,force_update=False,using=None,update_fields=None):
        self.slug = slugify(self.title)
        super(Article, self).save()



    def __str__(self):
        return f"{self.title} - {self.author}"

    # class Meta:
    #     ordering = ('-created','-updated')


class New(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.replace(' ','-')
        super(New,self).save(*args, **kwargs)

