from django import forms
from .models import Post, Image
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content',]
        # widgets = {
        #     'content' : forms.Textarea(),
        # }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ('post',)
        widgets = {
            'file' : forms.FileInput(attrs={'multiple' : True}),
        }