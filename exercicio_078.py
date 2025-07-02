#Faça um programa que leia 5 valores numéricos e guarde em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições.

num = []
for cont in range(0, 5):
    num.append(int(input('Digite um valor: ')))

maior = max(num)
menor = min(num)

print(f'\nVocê digitou os valores: {num}')
print(f'O maior valor foi {maior} nas posições:', end=' ')
for i, v in enumerate(num):
    if v == maior:
        print(i, end=' ')
print(f'\nO menor valor foi {menor} nas posições:', end=' ')
for i, v in enumerate(num):
    if v == menor:
        print(i, end=' ')
