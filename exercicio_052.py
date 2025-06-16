#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

p1 = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
for c in range(0, 10,):
    print(f'{p1 + rz * c}')