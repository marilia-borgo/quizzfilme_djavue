import json

import requests

from ..models import Personalidade


def contabilizaResultado(respostas, user):
    result_a=0
    result_b=0
    result_c=0
    for element in respostas:
        if element == 'a' or element=='a1':
            result_a=result_a+1
        if element == 'b' or element=='b1':
            result_b=result_b+1
        if element == 'c' or element=='c1':
            result_c=result_c+1
    
    if result_a > result_b and result_a > result_c:
        personalidade = 'Espírito Livre'
    if result_b > result_a and result_b > result_c:
        personalidade = 'Princesa'
    if result_c > result_b and result_c > result_b:
        personalidade = 'Perdedor'
    else:
        personalidade = 'Princesa'
    
    salvaPersonalidadeBanco(personalidade, user)

def salvaPersonalidadeBanco(personalidade, user):
    personalidade = Personalidade(resultado=personalidade, user_id=user)
    personalidade.save()

def pega_resultado(user):
    return decide_filmes(Personalidade.objects.get(user_id=user))

def decide_filmes(resultado):
    relacao_resultado_filme = {
        'Princesa': 164,
        'Espírito Livre': 6282,
        'Perdedor': 6282
    }
    r = requests.get(f"https://api.themoviedb.org/3/movie/{relacao_resultado_filme[resultado.resultado]}?api_key=6be3b0e227f0e67a222cdbe605a730e8&language=pt-br&page=1", auth=('user', 'pass'))
    filme =  json.loads(r.text)
    filme_info = {
        'titulo': filme['title'],
        'resumo': filme['overview'],
        'poster_path':filme['poster_path'],
        'personalidade': resultado.resultado
    }
    return filme_info
    



