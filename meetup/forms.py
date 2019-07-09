from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

from meetup.models import User, Group, Meetup


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('name','email','interests','host')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already taken")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        if self.clean_email() and self.clean_password2():
            user = super(RegisterForm, self).save(commit=False)
            user.set_password(self.cleaned_data.get('password1'))
            if commit:
                user.save()
            return user
        else:
            raise ValueError("Error in form")

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput,label="Password")

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user_final = User.objects.filter(
            Q(email__iexact = email)
        ).distinct()

        if not user_final.exists() and user_final.count() != 1:
            raise forms.ValidationError("Invalid credentials. User does not exist")

        user_obj = user_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError("Password incorrect")

        self.cleaned_data['user_obj'] = user_obj
        return super(LoginForm, self).clean()

class GroupForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('name','description','category','location','photo')

class MeetupForm(forms.ModelForm):

    class Meta:
        model = Meetup
        fields = ('name', 'description')
