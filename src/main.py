from GameFunctions import *

def main():
    pontuacao = {"jogador1": 0}
    colunas = 4 #int(input("Número de colunas: "))
    linhas = 4 #int(input("Número de linhas: "))
    while (colunas > 10 or linhas > 10):
        colunas = int(input("Número de colunas (menor ou igual a 10): "))
        linhas = int(input("Número de linhas (menor ou igual a 10): "))
    tabuleiro = [[0 for i in range(colunas)] for j in range(linhas)]
    caiGemas(tabuleiro, linhas, colunas)
    exibeTabuleiro(tabuleiro)
    verificaCadeia(pontuacao, tabuleiro, linhas, colunas)
    exibeTabuleiro(tabuleiro)
    print(pontuacao)
    print("indo pra permuta")
    linha1 = int(input())
    coluna1 = int(input())
    linha2 = int(input())
    coluna2 = int(input())
    permutaPosicao(pontuacao, tabuleiro, linha1, coluna1, linha2, coluna2, linhas, colunas)
    exibeTabuleiro
    print(pontuacao)

main()