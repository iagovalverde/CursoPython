'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²
'''

largura_parede = float(input('Largura da parede(m): '))
altura_parede = float(input('Altura da parede(m): '))
area_parede = largura_parede * altura_parede
litros_tinta = area_parede / 2
print(f'A parede de {area_parede}m² necessita de {litros_tinta}L de tinta')
