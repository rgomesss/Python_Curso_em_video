#Faça um programa que leia um número qualquer e mostre o seu fatorial.
#Ex: 5! = 5x4x3x2x1 = 120
print('Calculadora de fatorial!')

n = int(input('Digite um número para saber o seu fatorial: '))
c = 1
fatorial = n

while c < n:
    fatorial *= (n - c)
    c += 1
print(f'O fatorial de {n} é {fatorial}.')