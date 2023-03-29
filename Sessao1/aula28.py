"""
introdução ao try/except
try -> tenta executar o código
except -> ocorreu um erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que você digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2:.1f}.')
except:
    print('Isso não é um número.')    