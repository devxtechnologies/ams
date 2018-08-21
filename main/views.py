from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .mixins import SendSMSMixin

import datetime

# Create your views here.


class InitialView(LoginRequiredMixin, FormView):

    """
        InitialView: This view initialises the list of subjects available for the user and accepts
        the name of the subject that the attendance is being given for.
    """

    template_name = "initial.html"
    form_class = SubjectSelectForm
    success_url = reverse_lazy("home")

    def get_form_kwargs(self):
        kwargs = super(InitialView, self).get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def post(self, request, *args, **kwargs):
        self.request.session["teaches_pk"] = request.POST.get("teaches")
        return redirect(reverse_lazy("attendance"))


class AttendanceView(SendSMSMixin, LoginRequiredMixin, View):

    """
        AttendanceView: This view lists the students for the selected subject and accepts the
        absentee list for that particular subject fot that particular hour.
    """

    template_name = "attendance.html"
    url = "https://api.textlocal.in/send/?username=nandkeolyar.aayush@gmail.com&hash=19dd5bfe0649f20c9fa6e742b873a77c9bd18ea14368fc4e52914b4e8add2ab6&sender=TBMSCL&"

    def get(self, request, *args, **kwargs):
        context = {}
        teaches_pk = self.request.session.get("teaches_pk")
        teaches = Teaches.objects.get(pk=teaches_pk)
        student_list = User.objects.filter(
            subjects__in=[teaches.subject],
            sem=teaches.sem,
            sec=teaches.sec,
            department=teaches.department,
        )
        context["student_list"] = student_list
        context["teaches"] = teaches

        return render(self.request, self.template_name, context)

    def get_msg(self, name, klass):
        msg = f"Your ward {name} was absent for the class {klass}."
        return msg

    def post(self, request, *args, **kwargs):
        teaches = Teaches.objects.get(pk=self.request.session.get("teaches_pk"))
        attendance = Attendance.objects.create(teaches=teaches)
        student = request.POST.getlist("student")
        for i in student:
            user = User.objects.get(username=i)
            Absentees.objects.create(user=user, attendance=attendance)
        return redirect(reverse_lazy("initial"))
