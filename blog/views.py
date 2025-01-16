from django.shortcuts import render,get_object_or_404

from blog.models import Article, Category
from django.core.paginator import Paginator

# Create your views here.

def article_detail(request,slug):
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article,slug=slug)
    return render(request,'blog/post_details.html',{'article':article})

def articles_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')

    paginator = Paginator(articles, 4)
    object_list = paginator.get_page(page_number)
    return render(request,'blog/articles_list.html',{'articles_list':object_list})

def category_detail(request,pk):
    category = get_object_or_404(Category,id=pk)
    articles = category.articles.all()
    return render(request,'blog/articles_list.html',{'articles_list':articles})
