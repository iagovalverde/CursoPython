n = input('Digite algo: ')

print(f'{type(n)}',
      f'\nSó tem espaços? {n.isspace()}',
      f'\nÉ um numero? {n.isnumeric()}',
      f'\nÉ alfabético? {n.isalpha()}',
      f'\nÉ alfanumérico? {n.isalnum()}',
      f'\nEstá em maiusculas? {n.isupper()}',
      f'\nEstá em minúsculas? {n.islower()}',
      f'\nEstá capitalizado? {n.istitle()}'
)



