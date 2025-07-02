#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listar extrar que vão conter apenas os valores pares e ímpares digitados, respesctivamente. Ao final, mostre o conteúdos das três listas geradas

lista1 = []
while True:
    lista1.append(int(input('Digite um valor: ')))
    menu = input('Quer continuar ? [S][N]').upper()
    if menu != 'S':
        break
lista_pares = []
lista_impares = []
for num in lista1:
    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
print(f'Você digitou: {lista1}')
print(f'Lista com numeros pares: {lista_pares}')
print(f'Lista com numeros impares: {lista_impares}')