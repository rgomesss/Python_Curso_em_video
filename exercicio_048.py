#Faça um programa que calcule a soma entre todos os números ímpares que são multiplos de três e que se encontram no intervalo entre 1 até 500

s = 0

for c in range ( 1, 500, 2):
    if c % 3 == 0 :
        s += c
print(s)