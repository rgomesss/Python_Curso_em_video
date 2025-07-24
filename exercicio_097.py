#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
    print('-' * (len(msg)))
    print(msg)
    print('-' * (len(msg)))

escreva('        Rafael Gomes        ')
escreva('        Curso de Python        ')
escreva('        Clube de Regatas do Flamengo        ')