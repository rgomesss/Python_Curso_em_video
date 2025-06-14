#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço miliar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

atual = 2025
ano = int(input('Digite o ano do seu nascimento: '))
idade = atual - ano

if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE')
if idade < 18:
    saldo = 18 - idade
    print (f'Ainda falta {saldo} anos para o alistamento')
if idade > 18:
    saldo = idade - 18
    print(f'Voce ja deveria ter se alistado a {saldo} anos')