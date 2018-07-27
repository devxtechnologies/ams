from django import forms

from .models import Attendance, Teaches

class SubjectSelectForm(forms.ModelForm):
	class Meta:
		model = Attendance
		exclude = ('teacher', 'date_time',)

		def __init__(self, user, *args, **kwargs):
			self.user = user
			print(user)
			super(SubjectSelectForm, self).__init__(user, *args, **kwargs)
			self.fields['subject'].queryset = Teaches.objects.filter(teacher=user)