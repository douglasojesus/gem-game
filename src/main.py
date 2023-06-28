from GameFunctions import *
import View

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
    View.play(tabuleiro, colunas, linhas)

main()