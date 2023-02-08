import json

from django.http import JsonResponse

from .service import resultado


def recebe_resultado(request):
    respostas = request.POST['resultado']
    user = request.user.id
    resultado.contabilizaResultado(respostas, user)

    return JsonResponse({})

def get_resultado(request):
    user = request.user.id
    resultado = resultado.pegaResultado(user)
    return JsonResponse(resultado)