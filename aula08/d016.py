'''
crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''
from math import trunc

numero = float(input('Digite um numero: '))
numero_inteiro = trunc(numero)
print(f'O numero Real {numero} em Inteiro é: {numero_inteiro}')

