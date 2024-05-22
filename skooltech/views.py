from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .models import Student

def index(request):
    Student_list = Student.objects.all()
    template = loader.get_template('skooltech/index.html')
    context = {
        'Students': Student_list,
    }
    return HttpResponse(template.render(context, request))