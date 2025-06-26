#Crie um programa que leia vários números inteiros pelo teclado. o programa só vai parar quando o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag)

contador = soma = n = 0

while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    contador += 1
    soma += n
print(f'Você digitou {contador} números e a soma total é {soma}')
