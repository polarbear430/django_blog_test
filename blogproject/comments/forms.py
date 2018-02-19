from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
	"""docstring for CommentForm"""
	class Meta:
		"""docstring for Meta"""
		model = Comment
		fields=['name','email','url','text']
			
		