#forms.py under profile customization application
from django import forms
from users.models import Profile


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','occupation','location','profile_image','bio','first_question_option','second_question_option','third_question_option','fourth_question_option']