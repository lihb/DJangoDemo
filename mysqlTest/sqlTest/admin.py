#coding:utf8

from django.contrib import admin
from sqlTest.models import Publisher, Author, Book 


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'email')
	search_fields = ('first_name','last_name', 'email')     #左上角显示搜索栏

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publisher', 'publication_date') #显示可根据标签内容排序的表格
	list_filter = ('publication_date', 'publisher')           #页面右边显示一个快速查询器
	date_hierarchy = 'publication_date'                       #页面左上角显示一个逐层深入的导航条
	ordering = ('-publication_date',)                         #在'publication_date'标签上会出现一个倒三角形
	#fields = ('title', 'authors', 'publisher')
	#filter_horizontal = ('authors',)
	raw_id_fields = ('publisher',)


admin.site.register(Publisher)
#admin.site.register(Author)
admin.site.register(Author, AuthorAdmin)
#admin.site.register(Book)
admin.site.register(Book, BookAdmin)
