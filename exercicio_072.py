#Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado entre 0 e 20 e mostra-lo por extenso.

lista = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
         'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
         'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
         'dezenove', 'vinte')

num = -1
while num < 0 or num > 20:
    num = int(input('Digite um número entre 0 e 20: '))
    if num > 20 or num < 0:
        print('Tente novamente, digite um número entre 0 e 20: ')

print(f'Você digitou {lista[num]}')




