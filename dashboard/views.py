from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


from main.models import *

# Create your views here.


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        attendance = Attendance.objects.filter(teaches__teacher=self.request.user)
        context["attendance_list"] = attendance

        return context


class LogView(LoginRequiredMixin, TemplateView):
    """
	This is to show all the changes that have been made to the existing
	attendance.
	"""

    template_name = "dashboard/log.html"

    def get_context_data(self, **kwargs):
        context = super(LogView, self).get_context_data(**kwargs)

        return context


class ReportView(LoginRequiredMixin, TemplateView):
    """
	This is to show all the changes that have been made to the existing
	attendance.
	"""

    template_name = "dashboard/report.html"

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)

        return context
