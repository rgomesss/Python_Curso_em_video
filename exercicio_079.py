#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número ja exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente

num = []

while True:
    adicionar = int(input('Digite um valor: '))
    if adicionar in num:
        print('O valor ja está na lista')
    else:
        num.append(adicionar)
    menu = input('Quer continuar: [s][n]: ').lower()
    if menu != 's':
        break
print(f'Os números digitados foram: {sorted(num)}')

    


    
    