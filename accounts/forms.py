from django import forms
from django.contrib.auth import (get_user_model, authenticate)


User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Username"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={"placeholder":"Email"}), required=True)
    email2 = forms.EmailField(label="", widget=forms.EmailInput(attrs={"placeholder":"Confirm Email"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "email2",
            "password"
        ]

    def clean_email2(self):
        email = self.cleaned_data.get("email")
        email2 = self.cleaned_data.get("email2")
        if email != email2:
            raise forms.ValidationError("Email must match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email already registered")
        return email

class UserLoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Username"}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={"placeholder": "Password"}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect username or password")
            if not user.is_active:
                raise forms.ValidationError("This user is not active")
        return super(UserLoginForm, self).clean(*args, **kwargs)
