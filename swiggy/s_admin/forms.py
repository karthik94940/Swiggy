from django import forms

# admin State Form
from s_admin.models import *


class AdminStateForm(forms.ModelForm):
    class Meta:
        model = AdminStateModel
        exclude = ('state_id',)