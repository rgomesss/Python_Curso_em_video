#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e tambem indique o menor e o maior valor que estão na tupla

import random

numeros = tuple(random.randint(1, 60) for _ in range(5))
print(f'Números sorteados: {numeros}')
print(f'O menor número é : {min(numeros)}')
print(f'O maior número é : {max(numeros)}')

