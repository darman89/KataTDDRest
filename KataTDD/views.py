from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from KataTDD.models import Portafolio


@csrf_exempt
def index(request):
    portafolio_list = Portafolio.objects.all()
    return HttpResponse(serializers.serialize("json", portafolio_list))
