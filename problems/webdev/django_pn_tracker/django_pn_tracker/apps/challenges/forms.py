from django import forms
from . import models


# Learn about Django Model forms:
# https://docs.djangoproject.com/en/2.1/topics/forms/modelforms/
# Learn about Django form fields:
# https://docs.djangoproject.com/en/2.1/ref/forms/fields/
class AttendeeEditForm(forms.ModelForm):

    class Meta:
        fields = ['name', 'skills', 'challenge', 'date']
        model = models.AttendeeInfo


class ConfirmForm(forms.Form):
    pass