import random

CORES = ["A", "B", "C", "D"]

def verificaCadeia(): pass

def permutaPosicao(): pass

def destroiGemas(): pass

def caiGemas(tabuleiro, linhas, colunas): 
    #Percorre tabulerio
    for i in range(linhas):
        for j in range(colunas):
            if tabuleiro[i][j] == 0:
                tabuleiro[i][j] = random.choice(CORES)

def exibeTabuleiro(tabuleiro): 
    for linhas in tabuleiro:
        for colunas in linhas:
            print(colunas + " ", end='')
        print()

def exibeDica(): pass

def main():
    colunas = int(input("Número de colunas: "))
    linhas = int(input("Número de linhas: "))
    while (colunas > 10 or linhas > 10):
        colunas = int(input("Número de colunas (menor ou igual a 10): "))
        linhas = int(input("Número de linhas (menor ou igual a 10): "))
    tabuleiro = [[0 for i in range(colunas)] for j in range(linhas)]
    caiGemas(tabuleiro, linhas, colunas)
    exibeTabuleiro(tabuleiro)

main()