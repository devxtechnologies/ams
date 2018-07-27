from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
   url(r'^entry/', views.MainView.as_view(), name='main'),
]