'''
Crie um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada
'''

numero = int(input('Digite um numero: '))
dobro_numero = 2 * numero
triplo_numero = 3 * numero
raiz_quadrada_numero = numero**(1/2)

print(f'Numero {numero}',
      f'\nSeu dobro: {dobro_numero}'
      f'\nSeu triplo: {triplo_numero}'
      f'\nSua raiz quadrada: {raiz_quadrada_numero:.0f}'
)