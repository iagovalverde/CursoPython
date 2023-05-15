'''
UTILIZANDO MÓDULOS

import bebida            (importa todas as funcionalidades de um módulo)
from doce import cookie  (importa apenas as funcionalidades escolhidas)


math -> 
    ceil      (arredonda numero pra cima)
    floor     (arredonda numero pra baixo)
    trunc     (vai arredondar o numero, tirar a virgula dele deixando inteiro)
    pow       (potencia)
    sqrt      (raiz quadrada)
    factorial (calculo fatorial(?))
    hypot     (hipotenusa, tem q botar o cateto adj e o opost nos parenteses)
    cos       (cosseno)
    sin       (seno)
    tan       (tangente)


random ->
    random  (numero aleatorio(e necessario determina-lo, senao vai aparecer numero entre 0-1)
    randint (numero inteiro aleatorio)
    choice  (uma escolha de uma lista)
    shuffle (embaralha um lista)


import math                 (importa tudo)
from math import sqrt, ceil (importa apenas as funcionalidades sqrt e ceil)
'''

import math

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é {raiz}')


from math import sqrt

num = int(input('Digite um numero: '))
raiz = sqrt(num)
print(f'A raiz de {num} é {raiz}')


import random

num = random.randint(1,10)
print(num)
