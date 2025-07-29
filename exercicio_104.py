#Crie um programa que tenha uma função leiaint(), que vai funcionar de forma semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n=leiaint('Digite um n')

def leiaint(msg='Digite um número: '):
    while True:
        valor = input(msg)
        try:
            return int(valor)
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')


n = leiaint('Digite um n: ')
print(f'Você digitou o número {n}')