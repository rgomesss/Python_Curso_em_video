#''''
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixa de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Mádia 7.0 ou superior: Aprovado
#  ''

nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua nota: '))

media = (nota1 + nota2)/2

if media < 5:
    print('REPROVADO')
if media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO')
if media >= 7:
    print('APROVADO')