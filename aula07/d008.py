'''
Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
'''

medida_metros = float(input('Media em metros: '))
medida_centimetros = medida_metros * 100
medida_milimetros = medida_metros * 1000
print(f'Medida em m: {medida_metros} m \nMedida em cm: {medida_centimetros} cm' 
    f'\nMedida em mm: {medida_milimetros} mm')