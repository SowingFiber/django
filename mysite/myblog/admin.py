from django.contrib import admin
from .models import Post
from .models import Tweet

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'slug', 'author', 'publish', 'status')
    list_filter=('status', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields=('author',)
    date_hierarchy = 'publish'

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display=('tweet', 'slug', 'author', 'publish')
    list_filter=('publish', 'author')
    search_fields = ('tweet', 'author', 'publish')
    prepopulated_fields = {'slug': ('tweet',)}
    raw_id_fields=('author',)
    date_hierarchy = 'publish'
