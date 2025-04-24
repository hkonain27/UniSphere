from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Event, HousingListing, Message
# ---- USER REGISTRATION ----
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# ---- ROOM FORM ----
#class RoomForm(ModelForm):
  #  class Meta:
      #  model = Room
      #  fields = '__all__'
      #  exclude = ['host', 'participants']

# ---- PROJECT FORM ----
#class ProjectForm(forms.ModelForm):
  #  class Meta:
     #   model = Project
      #  fields = ['title', 'description', 'link']

# ---- EVENT FORM ----
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'time', 'major']

# ---- JOB SEARCH FORM ----
class JobSearchForm(forms.Form):
    title = forms.CharField(max_length=200, required=False, label="Job Title")
    location = forms.CharField(max_length=100, required=False, label="Location")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'title' in self.data:
            self.fields['title'].initial = self.data['title']
        if 'location' in self.data:
            self.fields['location'].initial = self.data['location']

# ---- HOUSING SEARCH FORM ----
class HousingSearchForm(forms.Form):
    location = forms.CharField(max_length=100, required=False, label="Location")

# ---- MESSAGE FORM ----
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']
