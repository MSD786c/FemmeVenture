from django import forms
from .models import Post  # Import your Post model

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['date', 'month', 'year', 'city_country', 'title', 'content']    