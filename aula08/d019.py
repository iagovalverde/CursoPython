'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
'''
from random import choice
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')

alunos = [n1, n2, n3, n4]
sorteado = choice(alunos)
print(f'O aluno sorteado foi: {sorteado}')