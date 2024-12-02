from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Include an email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Include username, email, and password fields
        
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'latitude', 'longitude']  # Remove 'date'

