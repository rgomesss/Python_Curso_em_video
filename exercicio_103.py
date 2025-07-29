#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que tenha algum dado não tenha sido informado corretamente

def ficha(nome='', gols=0):
    if not nome:
        nome = '<desconhecido>'
    try:
        gols = int(gols)
    except:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


ficha('Rafael', 3)
ficha('', 5)
ficha('Carlos')
ficha(gols=2)
ficha()