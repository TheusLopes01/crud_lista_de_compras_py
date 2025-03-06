import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir ' '[a]pagar ' '[l]istar: ')
    os.system('cls')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        if valor == '':
            print('Por favor, digite um valor')
        else:
            lista.append(valor)
    

    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')
        
        try:
         indice = int(indice_str)
         del lista[indice]
        except ValueError:
            print('Por favor, digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    
        
    elif opcao == 'l':
        os.system('cls')
        
        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)
    
    else:
        print('Por favor, escolha i, a ou l.')