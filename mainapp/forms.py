from django import forms

class CreatePostForm(forms.Form):
    tittle = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Post Tittle"}))
    author = forms.IntegerField(widget=forms.IntegerField(attrs={"class": "form-control", "placeholder": "author id"}))