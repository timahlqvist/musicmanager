from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Record

def index(request):
    all_records = Record.objects.all()
    context = {
        'all_records': all_records
    }
    return HttpResponse(template.render(context, request))

def details(request, record_id):
    return HttpResponse()