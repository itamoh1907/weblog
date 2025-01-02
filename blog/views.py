from django.shortcuts import render,get_object_or_404

from blog.models import Article


# Create your views here.

def article_details(request,pk):
    # article = Article.objects.get(id = pk)
    article = get_object_or_404(Article,id =pk)
    return render(request,'blog/post_details.html',{'article':article})
