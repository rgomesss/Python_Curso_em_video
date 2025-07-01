#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços organizando os dados em forma tabular.

produtos = (
    'Lápis', 1.50,
    'Caderno', 12.90,
    'Borracha', 0.99,
    'Estojo', 5.75,
    'Mochila', 89.90,
    'Caneta', 2.30,
    'Livro', 34.00
)

print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)

for i in range(0, len(produtos), 2):
    nome = produtos[i]
    preco = produtos[i+1]
    print(f'{nome:<30} R$ {preco:>7.2f}')

print('-' * 40)
