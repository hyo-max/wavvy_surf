from django.contrib import admin
from .models import Post, Category, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'title', 
        'author', 
        'hits',
        'pub_date',
        )


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)