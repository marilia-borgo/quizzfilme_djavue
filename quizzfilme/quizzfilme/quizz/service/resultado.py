from ..models import Personalidade


def contabilizaResultado(respostas):
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
    
    salvaPersonalidadeBanco(personalidade)

def salvaPersonalidadeBanco(personalidade):
    personalidade = Personalidade(resultado=personalidade)
    personalidade.save()

def get_resultado(user):
    resultado= Personalidade.filter(user_id=user)
    return resultado