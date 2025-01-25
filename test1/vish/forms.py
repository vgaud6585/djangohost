from django import forms
from .models import User

class UserForm(forms.ModelForm):
   class Meta:
       model = User
       fields = ['usr_name', 'usr_age', 'usr_image']