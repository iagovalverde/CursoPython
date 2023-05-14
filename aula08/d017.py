'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
'''

from math import hypot

cateto_oposto = float(input('Ingrese a medida do CO:'))
cateto_adjacente = float(input('Ingrese a medida do CA:'))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa mede {hipotenusa}')

# OUTRA FORMA

cateto_oposto = float(input('Ingrese a medida do CO:'))
cateto_adjacente = float(input('Ingrese a medida do CA:'))
hipotenusa = (cateto_oposto **2 + cateto_adjacente ** 2) ** (1/2)
print(f'A hipotenusa mede {hipotenusa}')
