#Crie um programa que crie uma função chamada voto() que vai receber o ano de nascimento de uma pessoa, retornando um valor literal incicando  se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓrio nas eleições
def voto(ano):
    idade = 2025 - ano  
    if idade < 16:
        return "VOTO NEGADO"
    elif 16 <= idade < 18 or idade > 65:
        return "VOTO OPCIONAL"
    else:
        return "VOTO OBRIGATÓRIO"

n = int(input('Em que ano você nasceu? '))
print(voto(n))