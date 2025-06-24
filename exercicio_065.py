#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valor lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

numero = soma = 0
contador = -1
while numero != 999:
    soma += numero
    numero = int(input('Digite um número [999 para parar]: '))
    contador += 1

print(f'Você digitou {contador} números e a soma entre eles é {soma}')