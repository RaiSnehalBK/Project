# main/forms.py
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'pager', 'specialization', 'department', 'experience', 'profile_pic']
