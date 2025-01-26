from django.urls import path

from . import views
app_name = 'blog'

urlpatterns = [
    path('detail/<slug:slug>',views.article_detail,name = 'article_details'),
    path('list/',views.articles_list,name = 'articles_list'),
    path('categories/<int:pk>',views.category_detail,name = 'category_details'),
    path('search/',views.search,name = 'search_articles'),
    path('contactus/',views.contactus,name = 'contactus'),

]