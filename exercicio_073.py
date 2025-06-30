#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a - Apenas os 5 primeiros colocados; b- os últimos 4 colocados da tabela; c- uma lista com os times em ordem alfabética; d- em que posição na tabela está o time da Chapecoense
tabela = ('Flamengo', 'Palmeiras', 'Botafogo', 'Corinthians', 'Cruzeiro',
          'Gremio', 'Internacional', 'Vasco', 'Atlético MG', 'Santos',
          'Chapecoense', 'Bahia', 'São Paulo', 'Bragantino', 'Vitória',
          'Sport', 'Fluminense', 'Mirassol', 'Ceará', 'Juventude')

alfa = sorted(tabela)

print(f'Os primeiros 5 colocados são: {tabela[0:5]}')
print(f'Os últimos 4 colocados são: {tabela[-4:]}')
print(f'Times em ordem alfabética: {alfa}')
print(f'A Chapecoense está na {tabela.index("Chapecoense") + 1}ª posição.')
