'''
 Crie um programa que leia dois valores e mostre um menu como esse abaixo:
 Seu programa deverá realizar a operação solicitada em casa caso
 [1] somar
 [2] multiplicar
 [3] maior
 [4] novos números
 [5] sair do programa
'''
import time
num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
sair = False

while not sair:
    print('''   [1] somar
   [2] multiplicar
   [3] maior
   [4] novos números
   [5] sair do programa                
''')
    
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        time.sleep(0.5)
        print(f'A soma entre {num1} e {num2} é {num1+num2}')
    time.sleep(0.5)
    if opcao == 2:
        time.sleep(0.5)
        print(f'O valor da multiplicação entre {num1} e {num2} é {num1*num2}')
    time.sleep(0.5)
    if opcao == 3:
        time.sleep(0.5)
        if num1 > num2 :
            print(f'O maior número é {num1}')
        if num1 < num2:
            print(f'O maior número é {num2}')
        else:
            print('Os dois números são iguais')
    time.sleep(0.5)
    if opcao == 4:
        time.sleep(0.5)
        num1 = int(input('Digite o novo valor: '))
        num2 = int(input('Digite o novo valor: '))
    time.sleep(0.5)
    if opcao == 5:
        sair = True
print('Fim')