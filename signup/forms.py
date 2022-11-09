# from django import forms
# from django.contrib.auth.models import User

# class signupForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name',"last_name",'email','password']

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import ValidationError
# from .models import Profile

class signUpForm(UserCreationForm):
	name = forms.CharField(label = ("Full Name"))
	username = forms.EmailField(label = ("Email"))

	class Meta:
		model = User
		fields = ('name', 'username', 'password1', 'password2')

