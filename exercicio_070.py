#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A - quando é o total gasto na compra. B - quantos produtos custam mais de R$ 1000. C - qual é o nome do produto mais barato

total = 0
produtos_mais_de_1000 = 0
menor_preco = 0
nome_mais_barato = ''

while True:
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    total += preco

    if preco > 1000:
        produtos_mais_de_1000 += 1

    
    if total == preco:  
        menor_preco = preco
        nome_mais_barato = nome
    elif preco < menor_preco:
        menor_preco = preco
        nome_mais_barato = nome

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar != 'S':
        break

print('\n===== RESULTADO DA COMPRA =====')
print(f'Você gastou R$ {total:.2f}')
print(f'Total de produtos com valor acima de R$ 1000: {produtos_mais_de_1000}')
print(f'O produto mais barato foi "{nome_mais_barato}" que custa R$ {menor_preco:.2f}')
