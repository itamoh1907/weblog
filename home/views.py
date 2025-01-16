from django.shortcuts import render
from django.urls import reverse


# Create your views here.
from blog.models import Article,New
def home(request):
    articles = Article.objects.all()
    # print(reverse('blog:article_details',kwargs={'pk':1,'number':9}))
    recent_articles = Article.objects.all().order_by('-created')[:3]

    return render (request,'home/index.html',context={'articles':articles})


def sidebar(request):
    context = {'name':'Aria'}

    return render(request,'includes/side_bar.html',context)