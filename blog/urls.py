from django.urls import path
from . import views
app_name='blog'

urlpatterns = [

    path('article/<int:pk>',views.article_details,name='article_details')
]