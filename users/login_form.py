from django import forms
 
class LoginForm(forms.Form):
    username=forms.CharField(label="username",max_length=64,required=True,error_messages={'required':'please enter your username'})
    password=forms.CharField(label="Password",widget=forms.PasswordInput,required=True,error_messages={'required':'this field is required'})