from django import forms
from . import models
from .models import Tutors

class CreateSchedule(forms.ModelForm):

    class Meta:
        model = Tutors
        fields = ['mon_start', 'mon_end', 'tue_start', 'tue_end', 'wed_start', 'wed_end', 'thur_start',
                  'thur_end', 'fri_start', 'fri_end', ]
