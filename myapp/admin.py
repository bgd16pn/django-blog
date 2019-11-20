from django.contrib import admin
from . import models


# class AuthorAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'email', 'created_on', 'last_logged_in')
# 	search_fields = ['name', 'email']
# 	ordering = ['name', '-last_logged_in']
# 	list_filter = ['active']
# 	date_hierarchy = 'created_on'


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	search_fields = ('name',)
	ordering = ('name',)


class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug')
	search_fields = ('name',)
	ordering = ('name',)


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'pub_date', 'author', 'category')
	search_fields = ['title', 'content']
	ordering = ['-pub_date']
	list_filter = ['pub_date']
	date_hierarchy = 'pub_date'
	# filter_horizontal = ('tags', )
	raw_id_fields = ('tags', )
	# prepopulated_fields = {'slug': ('title', )}
	readonly_fields = ('slug',)
	fields = ('title', 'slug', 'content', 'author', 'category', 'tags',)


class FeedbackAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'subject', 'date',)
	search_fields = ('name', 'email',)
	date_hierarchy = 'date'

# admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Feedback, FeedbackAdmin)