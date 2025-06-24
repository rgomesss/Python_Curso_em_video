#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No Final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

numero = soma = 0
contador = -1
while numero != 999:
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
    contador += 1

print(f'Você digitou {contador} números e a soma entre eles é {soma}')