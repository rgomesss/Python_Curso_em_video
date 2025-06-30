#Desenvolva um programa que leia quatro valores pelo teclado e guarde em uma tupla. No final, mostre: a- quantas vezes apareceu o número 9; b- em que posição foi digitado o primeiro valor 3; c- quais foram os números pares.

tupla = ()

for c in range(4):  
    num = int(input('Digite um número: '))
    tupla += (num,)

print(tupla)
print(f'O número 9 aparece {tupla.count(9)} vezes')

if 3 in tupla:
    print(f'O primeiro valor 3 aparece na posição {tupla.index(3)+1}')
else:
    print('O número 3 não foi digitado.')

print('Os números pares digitados foram:', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
