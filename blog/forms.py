from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['date','post']
        labels={"username":"Your Name","email":"email address"}