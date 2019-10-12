from django.contrib.auth import authenticate
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from KataTDD.models import Portafolio
from KataTDD.models import User, Imagen


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


@csrf_exempt
def get_view_public_info(request, user_id):
    if request.method == 'GET':
        portafolio = Portafolio.objects.get(usuario=user_id)
        images = Imagen.objects.filter(portafolio=portafolio, es_publica=True).select_related('portafolio').all()
        imagesList = list(images.values())
        result = [{'images': imagesList}]

    return JsonResponse(result, safe=False)


def user_login(request):
    user_params = json.loads(request.body)
    user = authenticate(username=user_params['username'], password=user_params['password'])
    if user is not None:
        return JsonResponse({'status': 'Authenticated'})
    else:
        return JsonResponse({'status': 'Error'})
