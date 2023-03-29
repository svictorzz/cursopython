"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de
índices inexistentes na lista.
"""
import os
lista_compras = []

while True:
    opcao = input('Selecione uma opção:\n'
              '[i]nserir [a]pagar [l]istar [s]air ')
    
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista_compras.append(valor)

    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        try:
            indice = int(indice_str)
            del lista_compras[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista.')  
        except Exception:
            print('Erro desconhecido.')    

    elif opcao == 'l':
        os.system('cls')
        if len(lista_compras) == 0:
            print('Nada para listar.')
        else:    
            for indice, nome in enumerate(lista_compras):
                print(indice, nome)
    elif opcao == 's':
        break    
    else:
        print('Digite uma opção válida (i, a ou l).')            
