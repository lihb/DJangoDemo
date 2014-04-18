from django.contrib import admin
from Blog.models import User, Blog

# Register your models here.

class UserAdmin(admin.ModelAdmin):
	list_display = ('username', 'sex',) 
	search_fields =('username', 'sex' ,'email')
	list_filter = ('username', 'sex')

class BlogAdmin(admin.ModelAdmin):
	list_display = ('author', 'title', 'content') 
	date_hierarchy = 'post_date'
	raw_id_fields = ('author',)

admin.site.register(User, UserAdmin)
admin.site.register(Blog, BlogAdmin)
