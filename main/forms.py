from django import forms

from .models import Attendance

class SubjectSelectForm(forms.ModelForm):
	class Meta:
		model = Attendance
		fields = ('__all__')
		exclude = ('user',)