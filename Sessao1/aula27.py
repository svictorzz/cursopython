"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade 
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        seu nome contém (ou não) espaços
        seu nome tem {n} letras
        a primeira letra do seu nome é {letra}
        a ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba:
        "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')


if nome and idade:
    print(f'Seu nome é: {nome}.')
    print(f'Seu nome invertido é: {nome[::-1]}.')

    if ' ' in nome:
        print('Seu nome contém espaços.')
    else:
        print('Seu nome não contém espaços.')  

    print(f'Seu nome contém {len(nome)} letras.')
    print(f'A primeira letra do seu nome é: {nome[0:1]}. ')
    print(f'A ultima letra do seu nome é: {nome[-1:]}.')

else:
    print('Desculpe, você deixou campos vazios.')    
