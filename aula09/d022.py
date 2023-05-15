'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome
'''

nome = input('Digite seu nome completo: ')

nome_maiscula = nome.upper()
nome_minuscula = nome.lower()
nomes = nome.split()
letras = ''.join(nomes)

print(f'Nome em maiuscula - {nome_maiscula}',
    f'\nNome em minuscula - {nome_minuscula}',
    f'\nQuantidade de letras - {len(letras)}',
    f'\nQuantidade de letras 1°Nome - {len(nomes[0])}')
