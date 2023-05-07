# Operadores Aritméticos

'''
Adição           +
Subtração        -
Multiplicação    *
Divisão          /
Potência         **
Divisão Inteira  //
Resto da divisão %

### Ordem de Precedência:
1- ()
2- **
3- * | / | // | % (quem aparecer primeiro)
4- + | -

Exemplos:
5 + 3 * 2 == 11
3 * 5 + 4 ** 2 == 31
3 * (5 + 4) ** 2 == 243
'''

palavra = 'Oi' + 'Olá'
print(palavra)

palavra = 'Oi' * 5
print(palavra)

palavra = '=' * 20
print(palavra)

'''
Alinhamento

(:<2) alinhar a direita
(:>2) alinhar a esquerda
(:^2) centralizado
(:=^10) nome centralizado com ===Nome===

'''
nome = input('Qual seu nome? ')
print(f'Prazer em te conhecer {nome:=^20}!')


n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'Soma: {s} - Multiplicação: {m} - Divisão: {d:.2f}',
      f'\nDivisão inteira: {di} - Exponenciação: {e}'
)

