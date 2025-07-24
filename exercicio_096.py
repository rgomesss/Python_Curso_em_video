#Faça um programa que tenha uma função chamado área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
def area (largura, comprimento):
    a = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {a}m².')
i = float(input('Largura do terreno (m): '))
c = float(input('Comprimento do terreno (m): '))
area(i, c)
    