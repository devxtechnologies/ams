from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *

import datetime
# Create your views here.


class InitialView(LoginRequiredMixin, FormView): 
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
		self.request.session['teaches_pk'] = request.POST.get('teaches')
		return redirect(reverse_lazy('attendance'))

  
class AttendanceView(LoginRequiredMixin, View):
	template_name = "attendance.html"

	def get(self, request, *args, **kwargs):
		context = {}
		teaches_pk = self.request.session.get('teaches_pk')
		teaches = Teaches.objects.get(pk=teaches_pk)
		student_list = User.objects.filter(subjects=teaches.subject, sem=teaches.sem, sec=teaches.sec)
		context['student_list'] = student_list
		context['sem'] = teaches.sem
		context['teacher_name'] = teaches.teacher.first_name

		return render(self.request, self.template_name, context)

	def post(self, request, *args, **kwargs):
		teaches = Teaches.objects.get(pk=self.request.session.get('teaches_pk'))
		attendance = Attendance.objects.create(teaches=teaches)
		student = request.POST.getlist('student')
		for i in student:
			user = User.objects.get(username=i)
			Absentees.objects.create(user=user, attendance=attendance)
		return redirect(reverse_lazy('initial'))

