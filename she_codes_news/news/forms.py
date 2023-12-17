from django import forms
from django.forms import ModelForm
from .models import NewsStory
from .models import Comment

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'category', 'image', 'content' ]
        widgets = {
            'pub_date': forms.DateInput(
                format='%m/%d/%Y',
                attrs={
                    'class':'form-control',
                    'placeholder':'Select a date',
                    'type':'date'
                }
            ),
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    #     widgets = {
    #     'content': forms.TextInput(attrs={'class': 'hidden-label'}),
    # }
