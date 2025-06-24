#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
p1 = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
termos = 10
contador = 0
while termos != 0:
    while termos != 0:
        print(f'{p1} -> ', end='')
        p1 += rz
        termos -= 1
        contador += 1
    print('PAUSA')
    termos = int(input('Quantos termos você quer mostrar a mais?'))
print(f'Progressão finalizada com {contador} termos exibidos.')