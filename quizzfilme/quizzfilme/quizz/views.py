import json

from django.http import JsonResponse

from .service import resultado


def recebe_resultado(request):
    respostas = request.POST['resultado']
    resultado.contabilizaResultado(respostas)

    return JsonResponse({})

def get_resultado(request):
    user= request.POST[user]
    resultado = resultado.pegaResultado(user)
    return JsonResponse({resultado})