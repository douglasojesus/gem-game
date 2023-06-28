import random

CORES = ["A", "B", "C", "D"]

'''def verificaCadeia(tabuleiro, linha1, coluna1, linha2, coluna2): 
    #Verifica se a posição da gema 2 monta cadeia na posição da gema 1
    gema1 = tabuleiro[linha1][coluna1]
    gema2 = tabuleiro[linha2][coluna2]
    if (gema2 == tabuleiro[linha1-1][coluna1-1]):'''


def permutaPosicao(tabuleiro, linha1, coluna1, linha2, coluna2):
    #Verifica se a permutação é possível
    if (linha1 == linha2+1 or linha2 == linha1+1 or linha1 == linha2):
        if (coluna1 == coluna2+1 or coluna2 == coluna1+1 or coluna1 == coluna2):
            if (tabuleiro[linha1][coluna1] != tabuleiro[linha2][coluna2]):
                if True: #verificaCadeia(tabuleiro, linha1, coluna1, linha2, coluna2):
                    buffer = tabuleiro[linha1][coluna1]
                    tabuleiro[linha1][coluna1] = tabuleiro[linha2][coluna2]
                    tabuleiro[linha2][coluna2] = buffer
                    print("Permutado")
                    return True
                #permuta
    print("Não foi possível permutar")
    return False
        


def destroiGemas(): pass

def primeiraExibixao(tabuleiro, linhas, colunas):
    #Percorre tabulerio
    for i in range(linhas):
        for j in range(colunas):
            if tabuleiro[i][j] == 0:
                tabuleiro[i][j] = random.choice(CORES)

def caiGemas(tabuleiro, linhas, colunas):
    for i in range(linhas):
        for j in range(colunas):
            if tabuleiro[i][j] == 0:
                if (i == 0):
                    tabuleiro[i][j] = random.choice(CORES)
                else:
                    tabuleiro[i][j] = tabuleiro[i-1][j]
                    tabuleiro[i-1][j] = 0
                caiGemas(tabuleiro, linhas, colunas)
    
def exibeTabuleiro(tabuleiro): 
    for linhas in tabuleiro:
        for colunas in linhas:
            print(colunas, " ", end='')
        print()

def exibeDica(): pass

def main():
    colunas = 4#int(input("Número de colunas: "))
    linhas = 4#int(input("Número de linhas: "))
    while (colunas > 10 or linhas > 10):
        colunas = int(input("Número de colunas (menor ou igual a 10): "))
        linhas = int(input("Número de linhas (menor ou igual a 10): "))
    tabuleiro = [[0 for i in range(colunas)] for j in range(linhas)]
    caiGemas(tabuleiro, linhas, colunas)
    exibeTabuleiro(tabuleiro)
    print()
    permutaPosicao(tabuleiro, 1, 1, 2, 1)
    exibeTabuleiro(tabuleiro)
    #primeiraExibixao(tabuleiro, linhas, colunas)



main()