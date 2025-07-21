#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela

aluno = {}
aluno["nome"] = input('Digite um nome: ')
aluno["media"] = float(input('Digite sua média: '))

if aluno['media'] < 7:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'

for k , v in aluno.items():
    print(f'{k} = {v}')