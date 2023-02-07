import json

from django.http import JsonResponse

from .service import resultado


def recebe_resultado(request):
    breakpoint()
    respostas = request.POST['resultado']
    user = request.POST['user']
    breakpoint()
    resultado.contabilizaResultado(respostas, user)

    return JsonResponse({})

def get_resultado(request):
    breakpoint()
    user= request.GET['user']
    breakpoint()
    resultado = resultado.pegaResultado(user)
    return JsonResponse({resultado})