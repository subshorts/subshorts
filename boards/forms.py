from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'is_private', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'is_private']
