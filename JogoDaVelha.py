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
        lugar = input(f"{jogador} em qual posição deseja jogar? ")
        if lugar not in ['1','2','3','4','5','6','7','8','9']:
            print("\nLugar inválido!")
            return realizarJogada(jogador, x)
        
        if verificarLugar(lugar):
            print("\nLugar ocupado!")
            continue

        tabuleiro[lugar] = x
        return


def verificarVitoria():
     # verticais
      if tabuleiro['7'] == tabuleiro['4'] == tabuleiro['1'] != ' ':
          return f"Vitória do jogador {tabuleiro['7']}", True
      elif tabuleiro['8'] == tabuleiro['5'] == tabuleiro['2'] != ' ':
          return f"Vitória do jogador {tabuleiro['8']}", True
      elif tabuleiro['9'] == tabuleiro['6'] == tabuleiro['3'] != ' ':
          return f"Vitória do jogador {tabuleiro['9']}", True

      # horizontais
      elif tabuleiro['7'] == tabuleiro['8'] == tabuleiro['9'] != ' ':
          return f"Vitória do jogador {tabuleiro['7']}", True
      elif tabuleiro['4'] == tabuleiro['5'] == tabuleiro['6'] != ' ':
          return f"Vitória do jogador {tabuleiro['8']}", True
      elif tabuleiro['1'] == tabuleiro['2'] == tabuleiro['3'] != ' ':
          return f"Vitória do jogador {tabuleiro['1']}", True

      #diagonais
      elif tabuleiro['7'] == tabuleiro['5'] == tabuleiro['3'] != ' ':
          return f"Vitória do jogador {tabuleiro['7']}", True
      elif tabuleiro['1'] == tabuleiro['5'] == tabuleiro['9'] != ' ':
          return f"Vitória do jogador {tabuleiro['1']}", True

      else:
          return [tabuleiro.values()].count(' '), False
      

jogador_x = ""
jogador_o = ""

def definirNome():
    global jogador_x, jogador_o
    jogador_x = input("Digite o nome do jogador X: ")
    jogador_o = input("Digite o nome do jogador O: ")


def jogar():
    definirNome()
    x = False
    while not x:
        mostra_velha()
        realizarJogada(jogador_x, 'X')
        jogador, x = verificarVitoria()
        if x:
            break
        mostra_velha()
        realizarJogada(jogador_o, 'O')
        jogador, x = verificarVitoria()
        if x:
            break
    print(jogador)
    

jogar()