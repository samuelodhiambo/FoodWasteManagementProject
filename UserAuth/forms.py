from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    # def save(self, commit: bool = True):
    #     user = super(CreateUserForm).save(commit=False)
    #     user.email = self.cleaned_data['email']
    #     user.username = self.cleaned_data['username']
    #     if commit:
    #         user.save()
    #     return user