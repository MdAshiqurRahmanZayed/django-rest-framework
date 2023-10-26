from django import forms 
from contact.models import Contact 
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import User
class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'autofocus': True}))


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, label='Username', required=True)

    class Meta:
        model = User
        fields = ['username', 'password']