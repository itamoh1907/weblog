from django.contrib import admin

# Register your models here.
from .models import Article,Category,New

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(New)