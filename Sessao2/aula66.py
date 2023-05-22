"""
Exercícios com funções

Crie uma função que multiplica todos os argumentos 
não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável.

---------------------------------------------------------------

Crie uma função que fala se o número é par ou ímpar.
Retorne se o número é par ou impar.

"""

def multi(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multi_1_2_3_4_5_6 = multi(1, 2, 3, 4, 5, 6)
print(multi_1_2_3_4_5_6)

# ----------------------------------------------------

def par_ou_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é par'
    return f'{numero} é impar'

teste1 = par_ou_impar(3)
print(teste1)    
