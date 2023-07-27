from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import User, Otpcode


class loginForm(forms.Form):
    phone_number = forms.CharField(max_length=11)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cd = super().clean()
        phone_number = cd.get('phone_number')
        if not phone_number:
            raise ValidationError('Enter your phone number')
        password = cd.get('password')
        if not password:
            raise ValidationError('Enter your password')
        user = User.objects.filter(phone_number=phone_number)
        if not user.exists() or not user[0].check_password(password):
            raise ValidationError('Phone number or password is wrong')


class VerifyCodeForm(forms.Form):
    code = forms.CharField(max_length=5)


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'email', 'phone_number']

    def clean_password2(self):
        cd = self.cleaned_data
        password1 = cd.get('password1')
        password2 = cd.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        if not password2:
            raise ValidationError("Password field can't be empty")
        return password2

    def clean_password1(self):
        cd = self.cleaned_data
        password1 = cd.get('password1')
        if not password1:
            raise ValidationError("Password field can't be empty")
        return password1

    def clean_email(self):
        cd = self.cleaned_data
        email = cd.get('email')
        check_email = User.objects.filter(email=email).exists()
        if check_email:
            raise ValidationError("Email already exists")
        return email

    def clean_phone_number(self):
        cd = self.cleaned_data
        phone = cd.get('phone_number')
        phone_check = User.objects.filter(phone_number=phone).exists()
        if phone_check:
            raise ValidationError("Phone number already exists")
        return phone

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you can change password using <a href=\"../password\">this form</a>")

    class Meta:
        model = User
        fields = ["email", "name", "phone_number",
                  "password", "is_active", "is_admin"]
