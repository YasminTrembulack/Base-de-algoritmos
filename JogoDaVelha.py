import os
RED     = "\033[1;31m"  
BLUE    = "\033[1;34m"
CYAN    = "\033[1;36m"
GREEN   = "\033[1;32m"
YELLOW  = "\033[1;33m"
MAGENTA = "\033[1;35m"
RESET   = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
GRAY_BOLD = "\033[1;30m"




tabuleiro ={'7': ' ' , '8': ' ' , '9': ' ',
            '4': ' ' , '5': ' ' , '6': ' ',
            '1': ' ' , '2': ' ' , '3': ' '}

def mostra_velha():
    os.system('cls')
    print("┌───┬───┬───┐")
    print(f"│ {printJogada('1')} │ {printJogada('2')} │ {printJogada('3')} │")
    print("├───┼───┼───┤")
    print(f"│ {printJogada('4')} │ {printJogada('5')} │ {printJogada('6')} │")
    print("├───┼───┼───┤")
    print(f"│ {printJogada('7')} │ {printJogada('8')} │ {printJogada('9')} │")
    print("└───┴───┴───┘")

def printJogada(x):
    if tabuleiro[x] == 'O':
        return MAGENTA + tabuleiro[x] + RESET
    elif tabuleiro[x] == 'X':
        return YELLOW + tabuleiro[x] + RESET
    else:
        return GRAY_BOLD + x + RESET
	

def verificarLugar(x):
    if tabuleiro[x] == 'O':
        return True
    elif tabuleiro[x] == 'X':
        return True
    return False


def realizarJogada(jogador, x):
    while True:
        mostra_velha()
        lugar = input(f"{jogador} em qual posição deseja jogar? ")
        if lugar not in ['1','2','3','4','5','6','7','8','9']:
            print("\nLugar inválido!")
            return realizarJogada(jogador, x)
        
        if verificarLugar(lugar):
            print("\nLugar ocupado!")
            continue

        tabuleiro[lugar] = x
        return verificarVitoria()


def verificarVitoria():
    global status
    # verticais
    if tabuleiro['7'] == tabuleiro['4'] == tabuleiro['1'] != ' ':
        status = f"Vitória do jogador {tabuleiro['7']}"
        return True
    elif tabuleiro['8'] == tabuleiro['5'] == tabuleiro['2'] != ' ':
        status = f"Vitória do jogador {tabuleiro['8']}"
        return True
    elif tabuleiro['9'] == tabuleiro['6'] == tabuleiro['3'] != ' ':
        status = f"Vitória do jogador {tabuleiro['9']}"
        return True

    # horizontais
    elif tabuleiro['7'] == tabuleiro['8'] == tabuleiro['9'] != ' ':
        status = f"Vitória do jogador {tabuleiro['7']}"
        return True
    elif tabuleiro['4'] == tabuleiro['5'] == tabuleiro['6'] != ' ':
        status = f"Vitória do jogador {tabuleiro['8']}"
        return True
    elif tabuleiro['1'] == tabuleiro['2'] == tabuleiro['3'] != ' ':
        status = f"Vitória do jogador {tabuleiro['1']}"
        return True

    #diagonais
    elif tabuleiro['7'] == tabuleiro['5'] == tabuleiro['3'] != ' ':
        status = f"Vitória do jogador {tabuleiro['7']}"
        return True
    elif tabuleiro['1'] == tabuleiro['5'] == tabuleiro['9'] != ' ':
        status = f"Vitória do jogador {tabuleiro['1']}"
        return True

    else:
        return False
      

jogador_x = ""
jogador_o = ""
status = ""

def definirNome():
    os.system('cls')
    global jogador_x, jogador_o
    jogador_x = input("Digite o nome do jogador X: ")
    jogador_o = input("Digite o nome do jogador O: ")


def jogar():
    definirNome()
    while True:
        if (realizarJogada(jogador_x, 'X')): break
        if (realizarJogada(jogador_o, 'O')): break
    os.system('cls')
    mostra_velha()
    print(status) 

jogar()