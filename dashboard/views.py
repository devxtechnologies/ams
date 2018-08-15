from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


from main.models import *

# Create your views here.


class DashboardView(LoginRequiredMixin, TemplateView):
    """
        DashboardView: This is the initial landing page of the dashboard.
        Some attendance statics are displayed in this page along with links to
        the following pages:

        1. /attendance/log/ (Access: Principal, Admin)
        2. /attendance/report/ (Access: Professors, Principal, Admin)

    """

    template_name = "dashboard/index.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        attendance = Attendance.objects.filter(teaches__teacher=self.request.user)
        context["attendance_list"] = attendance

        return context


class LogView(LoginRequiredMixin, TemplateView):
    """
        LogView: This is to show all the changes that have been made to the existing
        attendance.
    """

    template_name = "dashboard/log.html"

    def get_context_data(self, **kwargs):
        context = super(LogView, self).get_context_data(**kwargs)

        return context


class ReportView(LoginRequiredMixin, TemplateView):
    """
        ReportView: This is to show all the changes that have been made to the existing
        attendance.
    """

    template_name = "dashboard/report.html"

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)

        return context
