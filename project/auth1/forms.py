from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User




class signupform(UserCreationForm):
    class Meta:
        model=User
        fields= ['username','first_name','last_name','email']


class LogInFrom(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username','password']



