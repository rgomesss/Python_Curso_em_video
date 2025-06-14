#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
#Até 9 anos: Mirim
#Até 14 anos: infantil
#até 19 anos: Junio
#até 25 anos: Senior
#acima: Master

idade = int(input('Digite seu ano de nascimento:  '))
ano_atual = 2025

definir = ano_atual - idade

if definir <= 9:
    print('Mirim')
if definir > 9 and definir <=14:
    print('Infantil')
if definir > 14 and definir <=19:
    print('Junior')
if definir > 19 and definir <=25:
    print('Senior')
if definir > 25:
    print('Master')