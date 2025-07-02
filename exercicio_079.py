#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número ja exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente
import time
num = []

while True:
    adicionar = int(input('Digite um valor: '))
    time.sleep(0.5)
    if adicionar in num:
        time.sleep(0.5)
        print('O valor ja está na lista')
    else:
        num.append(adicionar)
    time.sleep(0.5)
    print('valor adicionado com sucesso ...')
    time.sleep(0.5)
    menu = input('Quer continuar: [s][n]: ').lower()
    time.sleep(0.5)
    if menu != 's':
        break
print(f'Os números digitados foram: {sorted(num)}')

    


    
    