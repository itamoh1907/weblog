from django.contrib import admin

# Register your models here.
from .models import Article,Category,New,Comment,Message

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(New)
admin.site.register(Comment)
admin.site.register(Message)