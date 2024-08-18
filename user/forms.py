from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Applicant

class ApplicantCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = Applicant
        fields = UserCreationForm.Meta.fields

class ApplicantChangeForm(UserChangeForm):
    class Meta:
        model = Applicant
        fields = UserChangeForm.Meta.fields

