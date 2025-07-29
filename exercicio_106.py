#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. OBS: utilize cores

def ajuda(comando):
    print('\033[44m', end='') 
    print(f"Acessando o manual do comando '{comando}'", end='')
    print('\033[m') 
    help(comando)


while True:
    print('\033[42m', end='')  
    comando = input('Função ou Biblioteca > ').strip()
    print('\033[m', end='')  

    if comando.upper() == 'FIM':
        print('\033[41mEncerrando o programa... Até logo!\033[m')
        break
    else:
        ajuda(comando)
