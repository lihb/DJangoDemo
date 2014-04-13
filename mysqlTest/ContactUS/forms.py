#coding:utf8


from django import forms

class ContactForm(forms.Form):
	subject = forms.CharField()
	email   = forms.EmailField(required = False, label='Your e-mail address') # 如不加label参数，默认在生成的html页面上的显示方式为：空格代替下划线，首字母大写，如果加了label参数，则以label参数的值为准 
	message = forms.CharField(widget = forms.Textarea)  # widget参数的使用

	def clean_message(self):
		message = self.cleaned_data['message']
		num_words = len(message.split())
		if num_words < 4:
			raise forms.ValidationError("Not enough words!")
		# message = 'hhesf'
		return message    #注意：必须有 return message，如没有，message的值将为None，如果message被修改，返回的将是修改后的值,原始数据将会丢失

