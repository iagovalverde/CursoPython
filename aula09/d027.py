'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza
'''

nome = input('Digite o nome completo: ')

lista_nome = nome.split()
primeiro_nome = lista_nome[0]
ultimo_nome = lista_nome[-1]

print(f'Primeiro nome: {primeiro_nome} \nÚltimo nome: {ultimo_nome}')