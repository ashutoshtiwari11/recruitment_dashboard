from django import forms
from .models import User

class MyUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'fname', 'lname', 'dob', 'email', 'img', 'address', 'state', 'country', 'city', 'resume', 'password']
