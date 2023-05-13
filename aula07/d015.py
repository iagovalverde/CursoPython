'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
'''

dias = int(input('Por quantos dias o carro foi alugado: '))
kilometros = float(input('Quantos Km foram percorridos: '))
custo_total = (dias * 60) + (kilometros * 0.15)
print(f'O aluguel do carro de {dias} dias percorrendo {kilometros}Km custou R${custo_total}')
