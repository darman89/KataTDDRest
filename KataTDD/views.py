from django.core import serializers
from django.http import HttpResponse
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from KataTDD.models import Portafolio
from .models import User


@csrf_exempt
def index(request):
    portafolio_list = Portafolio.objects.all()
    return HttpResponse(serializers.serialize("json", portafolio_list))


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        json_user = json.loads(request.body)
        username = json_user['username']
        first_name = json_user['first_name']
        last_name = json_user['last_name']
        password = json_user['password']
        email = json_user['email']
        foto = json_user['foto']
        perfil = json_user['perfil']

        user_model = User.objects.create_user(username=username, password=password)
        user_model.first_name = first_name
        user_model.last_name = last_name
        user_model.email = email
        user_model.foto = foto
        user_model.perfil = perfil
        user_model.save()

    return HttpResponse(serializers.serialize("json", [user_model]))
