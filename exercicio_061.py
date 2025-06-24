#Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while

p1 = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
contador = 0
while contador != 10:
    print(f'{p1 + rz * contador}')
    contador +=1
print('Fim')