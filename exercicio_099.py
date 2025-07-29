#Faça uma programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual é o maior.
def maior (*numeros):
    maior_num = max(numeros)
    print(f'O maior número foi: {maior_num}')
maior(4,5,6,7)


