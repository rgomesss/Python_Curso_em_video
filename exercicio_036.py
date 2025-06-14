#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado

valor = int(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário: '))
anos = int(input('Em quantos anos você vai pagar ? '))

meses = anos * 12
prestacao = valor / meses
limite = salario* 0.3

if prestacao <= limite:
    print('Emprestimo Aprovado')
else:
    print('Emprestimo Negado')