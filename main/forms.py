from django import forms

from .models import Attendance

class SubjectSelectForm(forms.ModelForm):
	class Meta:
		model = Attendance
		exclude = ('user',)