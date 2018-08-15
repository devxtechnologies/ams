from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    # /dashboard/ (Access: Professors, Principal, Admin)
    # Dashboard home page: Displays some statistics and quick access links.
    url(r"^$", views.DashboardView.as_view(), name="dashboard"),
    # /dashboard/log/ (Access: Principal, Admin)
    # Log page: All change logs are displayed here.
    url(r"^log$", views.LogView.as_view(), name="log"),
    # /dashboard/report/ (Access: Professors, Principal, Admin)
    # Report page: Attendance reports(weekly, monthly or yearly) are displayed here.
    url(r"^report$", views.ReportView.as_view(), name="report"),
]
