#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A - quantas pessoas tem mais de 18 anos. B - quantos homens foram cadastrados. C- Quantas mulheres tem menos de 20 anos

mais_de_18 = 0
homens = 0
mulheres_menos_20 = 0

while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)

    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    if idade > 18:
        mais_de_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        break

print('\n===== RESULTADO =====')
print(f'Total de pessoas com mais de 18 anos: {mais_de_18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres_menos_20}')

