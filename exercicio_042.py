#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar o tipo de triângulo será formado:
#Equilátero: todos os lados iguais
#Isóceles: dois lador iguais
#Escaleno: todos os lados diferentes


r1 = float(input('Digite o valor do primeiro segmento de reta: '))
r2 = float(input('Digite o valor do segundo segmento de reta: '))
r3 = float(input('Digite o valor do terceiro segmento de reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo.')

    if r1 == r2 == r3:
        print('Tipo: Equilátero (todos os lados iguais).')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Tipo: Isósceles (dois lados iguais).')
    else:
        print('Tipo: Escaleno (todos os lados diferentes).')
else:
    print('Os segmentos NÃO podem formar um triângulo.')