#Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: Quantidade de Notas, A maior nota, A menor nota, A média da turma, A situação(Opcional)

def notas(*n, sit=False):
    """
    Função para analisar notas e situações de alunos.
    
    Parâmetros:
    - n: uma ou mais notas dos alunos (aceita múltiplos valores).
    - sit: valor opcional, indicando se deve ou não adicionar a situação (default=False).
    
    Retorno:
    - dicionário com: total de notas, maior nota, menor nota, média e (opcional) situação.
    """
    resultado = {}
    resultado['Total'] = len(n)
    resultado['Maior'] = max(n)
    resultado['Menor'] = min(n)
    media = sum(n) / len(n)
    resultado['Média'] = media

    if sit:
        if media >= 7:
            resultado['Situação'] = 'Boa'
        elif media >= 5:
            resultado['Situação'] = 'Razoável'
        else:
            resultado['Situação'] = 'Ruim'

    return resultado


resp = notas(5.5, 7.0, 8.5, sit=True)
print(resp)
