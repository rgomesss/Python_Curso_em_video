#Escreva um programa que leia um número inteiro qualquer e peça para  o usuário escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal
import time
print(7*'-')
num = int(input('Digite um número '))
menu = int(input('''Digite [1] para Binário
Digite [2] para Octal
Digite [3] para Hexadecimal '''))
time.sleep(2)
print(7*'-')

if menu == 1:
    print(bin(num))
if menu == 2:
    print(oct(num))
if menu == 3:
    print(hex(num))
