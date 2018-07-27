from django import forms

from .models import Attendance, Teaches

class SubjectSelectForm(forms.ModelForm):
	class Meta:
		model = Attendance
		exclude = ('teacher', 'date_time',)

	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user')
		super(SubjectSelectForm, self).__init__(*args, **kwargs)
		self.fields['subject'].queryset = Teaches.objects.filter(teacher=self.user)