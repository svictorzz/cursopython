"""
while/else
"""
string = 'Churrasco'

i = 0
while i < len(string):
    letra = string[i]

    if letra == ' ':
        break

    print(letra)
    i +=1
else:
    print('Não há espaços na string.')
print('fora do while')       