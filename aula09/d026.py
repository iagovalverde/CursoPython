'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posição ela aparece a primeira vez
- Em que posição ela aparece a ultima vez
'''

frase = input('Digite uma frase: ')

quantidade_letra_a = frase.count('A')
primeiro_a = frase.find('A')
ultimo_a = frase.rfind('A')

print(f'Letra \'A\' aparece {quantidade_letra_a} vezes.',
    f'\nO primeiro \'A\' aparece na posição {primeiro_a}',
    f'\nO ultimo \'A\' aparece na posição {ultimo_a}')