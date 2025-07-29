#Faça uma função que tenha uma lista chamada números e duas funcões chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar a soma entre os valores PARES sorteados pela função anterios.
import random

números = []

def sorteia():
    for _ in range(5):
        n = random.randint(1, 100)
        números.append(n)
    print(f"Números sorteados: {números}")

def somaPar():
    soma = sum(n for n in números if n % 2 == 0)
    print(f"Soma dos números pares: {soma}")

# Exemplo de uso:
sorteia()
somaPar()
