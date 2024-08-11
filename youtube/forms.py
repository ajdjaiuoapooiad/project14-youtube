from django import forms
from .models import Post,Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        
        model=Post
        fields=['title','text','thumbnail','movie']
        
        def __str__(self):
            return self.title
        
class CommentCreateForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['title','text']
        
    