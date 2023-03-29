"""
enumerate -> enumera iterávies(índices)
"""

lista = ['Maria', 'Helena', 'Luiz']

# 1 possibilidade
for indice, nome in enumerate(lista):
    print(indice, nome)

# 2 possibilidade
for item in enumerate(lista):
    indice, nome = item
    print(item)