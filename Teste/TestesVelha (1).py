import os

#Variaveis
jogarNovamente="s"
jogadas=0
quemJoga=2 # 1=CPU e 2=Jogador
maxJogadas=9
vit="n"
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]
]
#Função que imprime o tabuleiro do jogo em matriz
def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0   "+ velha[0][0] + " | " + velha[0][1] + " | " + velha[0][2])
    print("   ---+---+---")
    print("1   "+ velha[1][0] + " | " + velha[1][1] + " | " + velha[1][2])
    print("   ---+---+---")
    print("2   "+ velha[2][0] + " | " + velha[2][1] + " | " + velha[2][2])
    print("Jogadas Realizadas: " + str(jogadas))

def vezJogador1():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga==2 and jogadas<maxJogadas:
        i=int(input("Jogador 1 - Linha...: "))
        j=int(input("Jogador 1 - Coluna..: "))
        try:
            while velha[l][c]!= " ":
                l=int(input("Jogador 1 - Linha...: "))
                c=int(input("Jogador 1 - Coluna..: "))
            velha[l][c]="X"
            quemJoga=1
            jogadas+=1
        except:
            print("Linha ou Coluna Invalida !!!")

def vezJogador2():
    global jogadas
    global quemJoga
    global maxJogadas
    if quemJoga==1 and jogadas<maxJogadas:
        i=int(input("Jogador 2 - Linha...: "))
        j=int(input("Jogador 2 - Coluna..: "))
        try:
            while velha[i][j]!= " ":
                i=int(input("Jogador 2 - Linha...: "))
                j=int(input("Jogador 2 - Coluna..: "))
            velha[i][j]="O"
            jogadas+=1
            quemJoga=2
        except:
            print("Linha ou Coluna Invalida !!!")


tela()
vezJogador1()
vezJogador2()

