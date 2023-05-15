### MANIPULANDO TEXTO ###


frase = 'Curso em Video Python'

#       C  u  r  s  o     e  m     V  i  d  e  o     P  y  t  h  o  n
#       0  1  2  3  4  5  6  7  8  9 10 11 12 13  14 15 16 17 18 19 20


# FATIAMENTO

print(frase[9])      # Mostra o caracter de indice 9

print(frase[9:13])   # Mostra a cadeia de caracteres começando do 9 ao 12

print(frase[9:21:2]) # Mostra a cadeia de caracteres começando do 9 ao 20, saltando de 2 em 2

print(frase[:5])     # Mostra do inicio ao 4

print(frase[15:])    # Mostra do indice 15 até o final

print(frase[9::3])   # Mostra do 9 até o final, saltando de 3 em 3

# ANALISE

print(len(frase))               # Mostra o comprimento da cadeia de caracteres = 21

print(frase.count('o'))         # Conta quantos 'o' possui a cadeia de caracteres

print(frase.count('o', 0, 13))  # Entre o caracter 0 ao 12 quantos 'o' existem -> 1

print(frase.find('deo'))        # Indica onde inicia 'deo' -> nesse caso 11

print(frase.find('Android'))    # String nao existe, retorna -1

'Curso' in frase                # Operador que retorna True se 'Curso' está em frase

# TRANSFORMAÇÃO

frase.replace('Python', 'Android')   # Substitui 'Python' por 'Android'

frase.upper()                        # Método que coloca tudo em maiusculas

frase.lower()                        # Método que coloca tudo em minusculas

frase.capitalize()                   # Coloca todos os caracteres em minusculas, apenas o 1 caracter fica em maiuscula

frase.title()                        # Coloca a primeira letra de cada palavra em maiuscula, o restante fica em minuscula

frase.strip()                        # Remove espaços inuteis no inicio e no final da string

frase.rstrip()                       # Remove espaços inuteis apenas no final da string 

frase.lstrip()                       # Remove espaços inuteis apenas no inicio da string 

# DIVISÃO

frase.split()      # Cria lista com as palavras de uma cadeia de caracteres (por padrão divide nos espaços)

# JUNÇÃO

'-'.join(frase)    # Junta os elementos de frase, e separa usando '-'

# ESCREVER TEXTOS LONGOS

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer venenatis eget odio eget auctor. In non lacinia ligula. Integer tempus ex eget aliquam ultrices. Cras facilisis pretium metus, at luctus mi scelerisque sed. Ut lobortis tortor quis tortor tristique, id dapibus nisi eleifend. Suspendisse rutrum aliquet nibh at congue. Mauris tincidunt scelerisque nulla, in porttitor massa interdum vitae. Proin dapibus tristique est. Suspendisse potenti. Aliquam erat volutpat. Integer nec massa eget velit venenatis tempus. Sed consequat velit at urna lobortis, sed porttitor est consequat. Donec vel ultricies justo. """)