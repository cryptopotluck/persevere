from .models import Question, Reply
from django.contrib.auth.forms import UserCreationForm
from django import forms
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Question
        fields = ['language', 'post_title', 'post_body']
        widgets = {
            'post_body': TinyMCE(),
        }

class ReplyForm(forms.ModelForm):
    """
       def __init__(self, *args, **kwargs):
           super(ReplyForm, self).__init__(*args, **kwargs)
           for field_name, field in self.fields.items():
               field.widget.attrs['class'] = 'form-control'
       """
    class Meta:
        model = Reply
        fields = ['reply_body']
        widgets = {
            'reply_body': TinyMCE(),
        }


form = PostForm()