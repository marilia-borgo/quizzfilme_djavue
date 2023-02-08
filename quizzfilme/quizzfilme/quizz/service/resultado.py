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

def get_resultado(user):
    resultado = Personalidade.objects.filter(user_id=user)
    decide_filmes(resultado)
    return resultado

def decide_filmes(resultado):
    if resultado == 'Princesa':
        r = requests.get('https://api.themoviedb.org/3/movie/164?api_key=6be3b0e227f0e67a222cdbe605a730e8&language=pt-br&page=1', auth=('user', 'pass'))
        filme = r['title']
        return filme
    
    if resultado == 'Espírito Livre':
        r = requests.get('https://api.themoviedb.org/3/movie/6282?api_key=6be3b0e227f0e67a222cdbe605a730e8&language=pt-br&page=1', auth=('user', 'pass'))
        filme = r['title']
        return filme
    
    if resultado == 'Perdedor':
        r = requests.get('https://api.themoviedb.org/3/movie/6282?api_key=6be3b0e227f0e67a222cdbe605a730e8&language=pt-br&page=1', auth=('user', 'pass'))
        filme = r['title']
        return filme



