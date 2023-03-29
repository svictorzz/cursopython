"""
Calculadora com while
"""
while True:
    
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input('Digite o operador(+-*/): ')
    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos == None:
        print('Um ou ambos os numeros são inválidos.') 
        continue   

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.') 
        continue       

    if operador == '+':
        soma = num1_float + num2_float
        print(f'{num1_float}+{num2_float} = {soma}')
    elif operador == '-':
        sub = num1_float - num2_float
        print(f'{num1_float}-{num2_float} = {sub}')
    elif operador == '*':
        multi = num1_float * num2_float
        print(f'{num1_float}x{num2_float} = {multi}')
    elif operador == '/':
        div = num1_float / num2_float
        print(f'{num1_float}/{num2_float} = {div}')          

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break