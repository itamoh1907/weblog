from django.shortcuts import render

# Create your views here.
from blog.models import Article,New
def home(request):
    articles = Article.objects.all()
    print(articles)
    print(type(articles))



    return render (request,'home/index.html',context={'articles':articles})