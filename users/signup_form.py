from django import forms
from django. contrib.auth.forms import UserCreationForm
from django. contrib.auth.models import User
class SignupForm(UserCreationForm):
    email=forms.EmailField(max_length=200,help_text='required')
    class meta:
        model=User
        
        field=('username','email','password1','password2')

        labels={
            'username':'username',
            'email':'Email',
            'password1':'Password',
            'password2':'Confirm Password'
        }
        
   


