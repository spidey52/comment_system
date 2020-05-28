from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

# @admin.register(Post)
# class PostsAdmin(admin.ModelAdmin):
# 	list_display = ('title', 'slug', 'author', 'publish', 'status')
# 	list_filter = ('status', 'created', 'publish', 'author')
# 	search_fields = ('title', 'author')
# 	prepopulated_fields = {'slug': ('title',)}
# 	raw_id_fields = ('author',)
# 	date_hierachy = 'publish'
# 	ordering = ('status', 'publish')

class PostAdmin(SummernoteModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	summernote_fields = ('body',)
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish', 'author')
	search_fields = ('title', 'author')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierachy = 'publish'
	ordering = ('status', 'publish')

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)