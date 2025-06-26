#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

vitorias = 0

while True:
    jogador = int(input('Digite um valor: '))
    escolha = input('Par ou Ímpar? [P/I] ').strip().upper()
    computador = randint(0, 10)
    total = jogador + computador
    resultado = 'P' if total % 2 == 0 else 'I'

    print(f'Você jogou {jogador} e o computador {computador}. Total = {total}')
    print('Deu PAR' if total % 2 == 0 else 'Deu ÍMPAR')

    if escolha == resultado:
        print('Você VENCEU!\n')
        vitorias += 1
    else:
        print('Você PERDEU!\n')
        break

print(f'GAME OVER! Você venceu {vitorias} vez(es).')
