from django import forms
from LoginReg.models import Reg

class RegForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)

        model=Reg
        widgets={'pwd':forms.PasswordInput}
        fields=['user','pwd']

class LoginForm(forms.Form):
    User = forms.CharField(max_length=40)
    Password = forms.CharField(widget=forms.PasswordInput)
