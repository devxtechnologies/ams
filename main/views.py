from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy


from .models import *
from .forms import *

import datetime
# Create your views here.

class MainView(FormView): 
	'''
	MainView: This view initialises the list of subjects available for the user and accepts 
	the name of the subject that the attendance is being given for.
	'''  
	template_name = "initial.html"
	form_class = SubjectSelectForm
	success_url = reverse_lazy("home")

	def get_context_data(self, *args, **kwargs):
		context = super(MainView, self).get_context_data(*args, **kwargs)
		subject_list = Teaches.objects.filter(teacher=self.request.user)
		self.request.session['subject_list'] = subject_list
		self.request.session['date_time'] = datetime.datetime.now()
		return context

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		return render(request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		create = forms.save(commit=False)
		create.teacher = self.request.user
		create.save()
		return redirect(reverse_lazy('main'))


class AttendanceView(TemplateView):
	template_name = "attendance.html"
	pass
