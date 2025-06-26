#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo



while True:
    num = int(input('Digite um número: '))
    if num < 0:
        break
    contador = 1
    while contador <= 10:
        resultado = num * contador
        print(f'{num} x {contador} = {resultado}')
        contador += 1
print('Fim')