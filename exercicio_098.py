#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada: a- de 1 até 10, de 1 em 1; b- de 10 até 0, de 2 em 2; c- Uma contagem personalizada.
from time import sleep
def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} em {passo}')

    if inicio<fim:
        c = inicio
        while c <= fim:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c+=passo
        print('FIM')

    else:
        c= inicio
        while c >= fim:
            print(f'{c} ', end='', flush=True)
            sleep(0.5)
            c-= passo
        print('FIM')
        

contador (1, 10, 1)
contador(10,1,2)

i = int(input('Digite o Inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))

contador(i,f,p)