#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

numpc = randint(0, 10)
palpites = 0
num = -1

while num != numpc:
    num = int(input('Adivinhe o número entre 0 e 10: '))
    palpites += 1
    if num < numpc:
        print('Mais...')
    elif num > numpc:
        print('Menos...')

print(f'Parabéns! Você acertou com {palpites} tentativa(s).')