from polls.models import Destination
from django.forms import ModelForm
class DestinationForm(ModelForm):
    class Meta:
          model=Destination
          fields='__all__'
          #fields=['name']
          
'''
from django import forms

class DestinationForm(forms.Form):
       name= forms.CharField(max_length=200)
       place= forms.CharField(max_length=200,widget=forms.Textarea)
'''
