from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    # /attendance/ (Access: Professors)
    # Initial page: This is where you select your class and subject.
    url(r"^$", views.InitialView.as_view(), name="initial"),
    # /attendance/entry/ (Access: Professors)
    # Attendance page: This is where you mark your attendance.
    url(r"^entry/", views.AttendanceView.as_view(), name="attendance"),
]
