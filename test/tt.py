from time import sleep
from interface import *
from system import *

# Programa Principal:
while True:
    cabecalho('Menu Principal')
    menu('1 - Adição', '2 - Subtração', '3 - Multiplicação', '4 - Divisão', '5 - Exponenciação')
    print('-' * 19)
    opcao = int(input('Sua opção: '))
    print('-' * 19)
    if opcao == 1:
        v1 = int(input('Digite um número: '))
        v2 = int(input('Digite outro número: '))
        resultado = calcular(v1, '+', v2)
        cabecalho(f'{v1} + {v2} = {resultado}')
        break
    elif opcao == 2:
        v1 = int(input('Digite um número: '))
        v2 = int(input('Digite outro número: '))
        resultado = calcular(v1, '-', v2)
        print(f'{v1} - {v2} = {resultado}')
        break
    elif opcao == 3:
        v1 = int(input('Digite um número: '))
        v2 = int(input('Digite outro número: '))
        resultado = calcular(v1, 'X', v2)
        print(f'{v1} X {v2} = {resultado}')
        break
    elif opcao == 4:
        v1 = int(input('Digite um número: '))
        v2 = int(input('Digite outro número: '))
        resultado = calcular(v1, '/', v2)
        print(f'{v1} / {v2} = {resultado}')
        break
    elif opcao == 5:
        v1 = int(input('Digite um número: '))
        v2 = int(input('Digite outro número: '))
        resultado = calcular(v1, '^', v2)
        cabecalho(f'{v1} ^ {v2} = {resultado}')
        break
    else:
        print('Opção inválida. Por favor Informe uma opção válida.')
        sleep(2)