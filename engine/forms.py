from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import MyUser


class CreateUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('username', 'email','secret_key', 'phone_number')

    def clean_password2(self):
        # password2 = self.cleaned_data.get("password2")
        # return password2
        pass


    def clean_secret_key(self):
        data = self.cleaned_data['secret_key']

        keys = {
            'dfWe3-4sda_', 
            'jd3dn-soPyt', 
            'bHGdf-t8sYT', 
            'dffds-SDsOR', 

            'dWdss-eE7Es',
            'dJerr-seFfe',
            'FDscs-sA*sd',
            'as34s-sfd)s',

            'mho98-dvEds',
            '4fHrd-dDasd',
            'dsfsU-ddfGd',
            '73#dd-GDdse',

            'OOIbt-3FERR',
            'hDDC8-JgFSS',
            'hTUH6-nmGFS',
            'SuTGX-uGRtW'

            }
        if data not in keys:
            raise forms.ValidationError("You have wrong key!")
        return data