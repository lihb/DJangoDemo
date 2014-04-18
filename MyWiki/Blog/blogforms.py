#coding:utf-8

from django import forms
from Blog.models import User

sex_choice=(
	('F', 'Female'),
	('M', 'Male'),
)

class UserForm(forms.Form):
	username = forms.CharField(label='姓名')
	password = forms.CharField(label='密码', widget = forms.PasswordInput)
	sex = forms.ChoiceField(label='性别', choices =sex_choice)
	email = forms.EmailField(label='邮箱', required = False)
	
	
class BlogForm(forms.Form):
	title = forms.CharField(label='标题')
	author = forms.ModelChoiceField(label='作者', queryset=User.objects.all())
	content = forms.CharField(label='内容', widget=forms.Textarea)


class LoginForm(forms.Form):
	username = forms.CharField(label='姓名')
	password = forms.CharField(label='密码', widget = forms.PasswordInput)


