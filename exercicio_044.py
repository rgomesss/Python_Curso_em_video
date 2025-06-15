#'''
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#- À vista dinheiro/cheque: 10% de desconto
#- À vista no cartão: 5% de desconto 
#- Em até 2x nmo cartão: preço normal
#- 3x ou mais no cartão: 20% de juros 
# '''

print('{:=^40}'.format(' LOJAS VEM Q TEM '))

print(' ')

preco = float(input('Digite o valor do produto: '))

print('''Qual será a forma de pagamento?

[ 1 ] para pagamento à vista no dinheiro ou no cheque

[ 2 ] para pagamento à vista no cartão

[ 3 ] para pagamento parcelado''')

cmd = int(input('Digite a forma de pagamento: '))



if cmd == 1:

    print('Para pagamento a vista no dinheiro ou no cheque o valor do produto será de {:.2f}R$'.format(preco*0.9))

elif cmd == 2:

    print('Para pagamento a vista no cartão o valor será de {:.2f} R$'.format(preco*0.95))

elif cmd == 3:

    parcela = int(input('Quantas parcelas: '))

    if parcela == 2:

        print('O valor será de 2 X {:.2f} R$, totalizando {:.2f} R$'.format(preco/parcela, preco))

    else:

        print('O valor será de {} X de {:.2f} R$, totalizando {:.2f} R$'.format(parcela, (preco*1.2)/parcela, preco*1.2))

else:

    print('\033[1;31mCOMANDO INEXISTENTE\033[m, tente novamente')