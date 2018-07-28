from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy


from .models import *
from .forms import *

import datetime
# Create your views here.

class InitialView(FormView): 
	'''
	InitialView: This view initialises the list of subjects available for the user and accepts 
	the name of the subject that the attendance is being given for.
	'''  
	template_name = "initial.html"
	form_class = SubjectSelectForm
	success_url = reverse_lazy("home")

	def get_form_kwargs(self):
		kwargs = super(InitialView, self).get_form_kwargs()
		kwargs.update({'user': self.request.user})
		return kwargs

	def post(self, request, *args, **kwargs):
		self.request.session['subject_pk'] = request.POST.get('subject')
		return redirect(reverse_lazy('main'))


class AttendanceView(TemplateView):
	template_name = "attendance.html"
	pass
