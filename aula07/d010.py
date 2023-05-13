'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar. Considere US$1,00 = R$3,27
'''

reais = float(input('Ingresse o valor em reais R$'))

dolares = reais / 3.27
print(f'Voce pode comprar US${dolares}')