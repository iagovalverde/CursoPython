'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle

a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')

alunos = [a1, a2, a3, a4]
shuffle(alunos)
print(f'A ordem de apresentaçao dos alunos é: {alunos}')