from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy


from .models import *
from .forms import *

import datetime
# Create your views here.

class InitialView(FormView): 
	'''
	MainView: This view initialises the list of subjects available for the user and accepts 
	the name of the subject that the attendance is being given for.
	'''  
	template_name = "initial.html"
	form_class = SubjectSelectForm
	success_url = reverse_lazy("home")

	def get_context_data(self, *args, **kwargs):
		context = super(InitialView, self).get_context_data(*args, **kwargs)
		context['form'] = SubjectSelectForm(user=self.request.user)
		return context

	def post(self, request, *args, **kwargs):
		return redirect(reverse_lazy('main'))


class AttendanceView(TemplateView):
	template_name = "attendance.html"
	pass
