from django import forms
from django.core.exceptions import ValidationError
from .models import Author, Tag, Category, Post, Feedback
from django.template.defaultfilters import slugify

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = '__all__'

	def clean_name(self):
		name = self.cleaned_data['name']
		name_l = name.lower()
		if name_l == 'admin' or name_l == 'author':
			raise ValidationError('Author name cannot be "admin/author"')
		return name_l

	def clean_email(self):
		return self.cleaned_data['email'].lower()

class TagForm(forms.ModelForm):
	author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
	
	class Meta:
		model = Tag
		fields = '__all__'

	def clean_name(self):
		name = self.cleaned_data['name']
		name_l = name.lower()
		if name_l == 'tag' or name_l == 'add' or name_l == 'update':
			raise ValidationError('Tag name cannot be "{}"'.format(name))
		return name

	def clean_slug(self):
		return self.cleaned_data['slug'].lower()


class CategoryForm(forms.ModelForm):
	author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
	class Meta:
		model = Category
		fields = '__all__'

	def clean_name(self):
		name = self.cleaned_data['name']
		name_l = name.lower()
		if name_l == 'tag' or name_l == 'add' or name_l == 'update':
			raise ValidationError('Category name cannot be "{}"'.format(name))
		return name

	def clean_slug(self):
		return self.cleaned_data['slug'].lower()


class PostForm(forms.ModelForm):
	author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False) 

	class Meta:
		model = Post
		fields = ('title', 'content', 'author', 'category', 'tags')

	def clean_name(self):
		title = self.cleaned_data['title']
		title_l = title.lower()
		if title_l == 'post' or title_l == 'add' or title_l == 'update':
			raise ValidationError('Post name cannot be "{}"'.format(title))
		return title

	def clean(self):
		cleaned_data = super(PostForm, self).clean()
		title = cleaned_data.get('title')
		if title:
			cleaned_data['slug'] = slugify(title)
		return cleaned_data

class FeedbackForm(forms.ModelForm):
	
	class Meta:
		model = Feedback
		fields = '__all__'
