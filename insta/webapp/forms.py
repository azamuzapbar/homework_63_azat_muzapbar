from django import forms
from webapp.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description', 'image']
        widgets = {'description': forms.TextInput(attrs={'class': 'form-control'}),
                   'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {'text': forms.TextInput(attrs={'class': 'form-control'})}


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))