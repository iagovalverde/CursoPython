'''
Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
'''

from math import cos, sin, tan, radians

angulo = float(input('Digite um angulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O angulo de {angulo}° tem seno{seno}, cosseno{cosseno} e tangente{tangente}')
