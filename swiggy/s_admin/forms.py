from django import forms

# admin State Form
from s_admin.models import *

#Admin State Form
class AdminStateForm(forms.ModelForm):
    class Meta:
        model = AdminStateModel
        exclude = ('state_id',)

#admin City Form

class AdminCityForm(forms.ModelForm):
    class Meta:
        model = AdminCityTable
        exclude = ('city_id',)

# admin Area Form
class AdminAreaForm(forms.ModelForm):
    class Meta:
        model = AdminAreaModel
        exclude = ('area_id',)