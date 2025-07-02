#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: a- Quantos números foram digitados; b- A lista de valores ordenada de forma decrescente; c- Se o valor 5 foi digitado e está ou não na lista

lista =[]
while True:
    lista.append(int(input('Digite um valor: ')))
    menu = input('Quer continuar ? [S][N]').upper()
    if menu != 'S':
        break

print(f'Você digitou: {len(lista)} números')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('Você digitou o numero 5')
else:
    print('O número 5 não está na lista')