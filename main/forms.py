from django import forms

from .models import Attendance, Teaches, Absentees
from django.forms import modelformset_factory


class SubjectSelectForm(forms.ModelForm):
    """
        SubjectSelectForm: 
    """
    class Meta:
        model = Attendance
        exclude = ("date_time",)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(SubjectSelectForm, self).__init__(*args, **kwargs)
        self.fields["teaches"].queryset = Teaches.objects.filter(
            teacher=self.user)
