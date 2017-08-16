from django import forms
from .models import Post

class Pform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post_title', 'post_text', 'post_author')