#Escreva um programa que leia um número n interiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
#Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8

num = int(input('Digite um número: '))
cont = fib = 0
fib1 = 1
while cont < num:
    print('{} {} '.format(fib,fib1),end='')
    fib += fib1
    fib1 += fib
    cont += 1