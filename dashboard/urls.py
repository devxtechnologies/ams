from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
	url(r'^$', views.DashboardView.as_view(), name='dashboard'),
	url(r'^log$', views.LogView.as_view(), name='log'),
]