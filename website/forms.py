from django import forms
from .models import Blog, Comment

class UploadForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('blog_title', 'blog_content', 'thumbnail')
        widgets = {
            "blog_title": forms.TextInput(attrs={"cols": 50, "rows": 10, 'class': "form-control"}),
            "blog_content": forms.Textarea(attrs={"cols": 50, "rows": 10, 'class':"form-control"}),
            "thumbnail": forms.TextInput(attrs={"cols": 50, "rows": 10, 'class': "form-control"}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            "comment": forms.TextInput(attrs={"cols": 50, "rows": 10, 'class': "form-control"}),
        }
