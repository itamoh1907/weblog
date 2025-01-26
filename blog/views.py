from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Article, Category
from django.core.paginator import Paginator
from .forms import MessageForm
from .models import Message
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


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, 'blog/articles_list.html', {'articles_list': object_list})


# def contactus(request):
#     if request.method == 'POST':
#         form = ContactUsForm(data=request.POST)
#         # print(form)
#         if form.is_valid():
#             print(form.cleaned_data['text'])
#             print(form.cleaned_data['name'])
#             return render(request, 'blog/contact_us.html', {'form': form})
#
#
#     else:
#         form = ContactUsForm()
#
#     return render(request,'blog/contact_us.html',{'form':form})
def contactus(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.age+=5
            instance.save()
            # Optionally clear the form and show a success message
            return render(request, 'blog/contact_us.html', {'form': form})


    else:
        form = MessageForm()

    return render(request, 'blog/contact_us.html', {'form': form})