from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
class ContactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Your name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder": "Your email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder": "Type your query here.."}))

def clean_email(self):
    email = self.cleaned_data.ger("email")
    if not "@" in email:
        raise forms.ValidationError("Use the correctt email format")
    return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirm password",widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already taken")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Already a account with is email , please try logging in!")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password2 != password:
            raise forms.ValidationError("Passwords must match")
        return data
