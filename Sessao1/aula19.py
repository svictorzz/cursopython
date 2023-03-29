# Exercicio para comparar qual valor do input é maior

primeiro_valor = input('Digite um número: ')
segundo_valor = input('Digite outro número: ')

int_primeiro = int(primeiro_valor)
int_segundo = int(segundo_valor)

if int_primeiro > int_segundo:
    print(f'{primeiro_valor} é maior que {segundo_valor}.')
elif int_segundo > int_primeiro:
    print(f'{segundo_valor} é maior que {primeiro_valor}.')
else:
    print(f'{primeiro_valor} é igual a {segundo_valor}.')   
