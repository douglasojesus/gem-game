from GameFunctions import *

def main():
    colunas = 4#int(input("Número de colunas: "))
    linhas = 4#int(input("Número de linhas: "))
    pontuacao = {"jogador1": 0}
    while (colunas > 10 or linhas > 10):
        colunas = int(input("Número de colunas (menor ou igual a 10): "))
        linhas = int(input("Número de linhas (menor ou igual a 10): "))
    tabuleiro = [[0 for i in range(colunas)] for j in range(linhas)]
    caiGemas(tabuleiro, linhas, colunas)
    pontuacao = verificaCadeia(pontuacao, tabuleiro, linhas, colunas)
    exibeTabuleiro(tabuleiro)
    print(pontuacao["jogador1"])

main()