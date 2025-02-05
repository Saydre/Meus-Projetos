import os

# Variáveis
jogarNovamente = "s"
jogadas = 0
quemJoga = 2  # 1=Jogador 1 e 2=Jogador 2
maxJogadas = 9
velha = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Função que imprime o tabuleiro do jogo em matriz
def tela():
    global velha
    global jogadas
    os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela
    print("    0   1   2")
    print("0   " + velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   ---+---+---")
    print("1   " + velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   ---+---+---")
    print("2   " + velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas Realizadas: " + str(jogadas))

def verificar_vitoria():
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if velha[i][0] == velha[i][1] == velha[i][2] != " ":
            return True
        if velha[0][i] == velha[1][i] == velha[2][i] != " ":
            return True
    if velha[0][0] == velha[1][1] == velha[2][2] != " ":
        return True
    if velha[0][2] == velha[1][1] == velha[2][0] != " ":
        return True
    return False

def vezJogador(jogador):
    global jogadas
    global quemJoga
    simbolo = "X" if jogador == 1 else "O"
    while True:
        try:
            i = int(input(f"Jogador {jogador} - Linha...: "))
            j = int(input(f"Jogador {jogador} - Coluna..: "))
            if velha[i][j] == " ":
                velha[i][j] = simbolo
                jogadas += 1
                quemJoga = 2 if jogador == 1 else 1
                break
            else:
                print("Posição já ocupada! Tente novamente.")
        except (ValueError, IndexError):
            print("Linha ou Coluna Inválida! Tente novamente.")

# Loop principal do jogo
while jogarNovamente.lower() == "s":
    jogadas = 0
    velha = [[" ", " ", " "] for _ in range(3)]  # Reseta o tabuleiro
    while jogadas < maxJogadas:
        tela()
        vezJogador(1)
        if verificar_vitoria():
            tela()
            print("Jogador 1 (X) venceu!")
            break
        if jogadas >= maxJogadas:
            break
        
        tela()
        vezJogador(2)
        if verificar_vitoria():
            tela()
            print("Jogador 2 (O) venceu!")
            break

    if jogadas == maxJogadas:
        tela()
        print("Empate!")

    jogarNovamente = input("Deseja jogar novamente? (s/n): ")

print("Obrigado por jogar!")