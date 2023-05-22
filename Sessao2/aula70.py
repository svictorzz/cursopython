"""
- Dicionários em Python (tipo dict)
- Dicionários são estruturas de dados do tipo 
par de "chave" e "valor".
- Chaves podem ser consideradas como o "índice"
que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc.
- O valor pode ser de qualquer tipo, incluindo outro dicionário.
- Usamos as chaves - {} - ou a classe dict para criar
dicionários.
- Imutáveis: str, int, float, bool, tuple
- Mutável: dict, list
"""
pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Souza',
    'idade': 20,
    'altura': 1.92,
    'enderecos': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 13}
    ],
}

for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')