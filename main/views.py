from django.shortcuts import render

# Create your views here.



class MainView(TemplateView):
    template_name = "attendance.html"
    