'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou nao com o nome 'SANTO'
'''

cidade = input('Digite o nome da cidade: ')

inicio_cidade = 'SANTO' in cidade[0:5]

print(inicio_cidade)