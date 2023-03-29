# Formatação de strings com o método format
a = 'Victor'
b = 'Caio'
c = 1.5

string = 'a={nome1} b={nome2} a={nome1} c={num1:.3f}'
formato = string.format(nome1 = a, nome2 = b, num1 = c)

print(formato)