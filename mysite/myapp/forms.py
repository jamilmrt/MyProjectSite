from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Person
 
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_description', 'project_image', 'project_link']
        widget = {
            'project_description': forms.Textarea(attrs={'rows': 4}),
        }
    

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = [
            'person_name',
            'person_image',
            'person_bio',
            'person_phone',
            'person_email',
            'person_github',
            'person_linkedin',
            'person_twitter',
            'person_facebook',
            'person_instagram',
            'person_website'
        ]
        widgets = {
            'person_bio': forms.Textarea(attrs={'rows': 4}),
        }