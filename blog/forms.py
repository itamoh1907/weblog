from django import forms
from .models import Message,Article
from django.core.validators import ValidationError


class MessageForm(forms.ModelForm):
    # title = forms.CharField(label='Title',max_length=100)
    # text = forms.CharField(widget=forms.Textarea)
    # email=forms.EmailField()
    class Meta:
        model = Message
        fields ='__all__'
        widgets={

            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Title','style':'width:500px;'}),
            'text':forms.Textarea(attrs={'class':'form-control','placeholder':'Text','style':'width:300px;'}),



        }

