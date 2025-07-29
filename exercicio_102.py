#Crie um programa que tenha uma função fatorial(), que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será  um valor lógico(opcional)indicando se será mostrado ou não na tela o processo de cálculo do fatorial

def fatorial(num=1, show=False):
    f = 1
    if show:
        for c in range(num, 0, -1):
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            f *= c
        print(f'= {f}')
    else:
        for c in range(num, 0, -1):
            f *= c
    return f

fatorial(5, show=True)
