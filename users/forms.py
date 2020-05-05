from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)
        del self.fields['password1']
        del self.fields['password2']


    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'phone_number',  'secret_key')

    def clean_secret_key(self):
        data = self.cleaned_data['secret_key']
        keys = {
          'dfWe3-4sda_', 
          'jd3dn-soPyt', 
          'bHGdf-t8sYT', 
          'dffds-SDsOR', 
          'dWdss-eE7Es'
        }
        if data not in keys:
            raise forms.ValidationError("You have wrong key!")
        return data


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'secret_key')




    