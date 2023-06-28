import random

CORES = ["A", "B", "C", "D"]

def destroiGema(tabuleiro, posicaoLinha, posicaoColuna): 
    tabuleiro[posicaoLinha][posicaoColuna] = 0

#Função percorre todas as gemas, verifica suas adjacências e remove as cadeias.
#Dá para refatorar!!!!!
def verificaCadeia(pontuacao, tabuleiro, linhas, colunas): 
    for i in range(linhas):
        for j in range(colunas):
            gemasIguaisVerticais = gemasIguaisHorizontais = 1 #A gema atual é igual a ela mesma
            posicoesGemasVerticais = [(i, j)]
            posicoesGemasHorizontais = [(i, j)]
            gemaAtual = tabuleiro[i][j]
            #Verifica gema de cima da gema atual
            aux = i
            while (aux > 0 and tabuleiro[aux-1][j] == gemaAtual):
                gemasIguaisVerticais += 1
                posicoesGemasVerticais.append((aux-1, j))
                aux -= 1
            #Verifica gema debaixo da gema atual
            aux = i
            while (aux < linhas-1 and tabuleiro[aux+1][j] == gemaAtual):
                gemasIguaisVerticais += 1
                posicoesGemasVerticais.append((aux+1, j))
                aux += 1
            #Verifica pontuação das gemas iguais verticais e destrói gemas
            if (gemasIguaisVerticais >= 3):
                exibeTabuleiro(tabuleiro)
                for m in range(len(posicoesGemasVerticais)):
                    destroiGema(tabuleiro, posicoesGemasVerticais[m][0], posicoesGemasVerticais[m][1])
                    pontuacao += 1
                exibeTabuleiro(tabuleiro)
                caiGemas(tabuleiro, linhas, colunas)
            #Verifica gema do lado esquerdo da gema atual
            aux = j
            while (aux > 0 and tabuleiro[i][aux-1] == gemaAtual):
                gemasIguaisHorizontais += 1
                posicoesGemasHorizontais.append((i, aux-1))
                aux -= 1
            #Verifica gema do lado direito da gema atual
            aux = j
            while (aux < colunas-1 and tabuleiro[i][aux+1] == gemaAtual):
                gemasIguaisHorizontais += 1
                posicoesGemasHorizontais.append((i, aux+1))
                aux += 1
            if (gemasIguaisHorizontais >= 3):
                exibeTabuleiro(tabuleiro)
                for m in range(len(posicoesGemasHorizontais)):
                    destroiGema(tabuleiro, posicoesGemasHorizontais[m][0], posicoesGemasHorizontais[m][1])
                    pontuacao += 1
                exibeTabuleiro(tabuleiro)
                caiGemas(tabuleiro, linhas, colunas)
    return pontuacao

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
    print("Não foi possível permutar")
    return False

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
    print()

def exibeDica(): pass

def main():
    colunas = 4#int(input("Número de colunas: "))
    linhas = 4#int(input("Número de linhas: "))
    pontuacao = 0
    while (colunas > 10 or linhas > 10):
        colunas = int(input("Número de colunas (menor ou igual a 10): "))
        linhas = int(input("Número de linhas (menor ou igual a 10): "))
    tabuleiro = [[0 for i in range(colunas)] for j in range(linhas)]
    caiGemas(tabuleiro, linhas, colunas)
    pontuacao = verificaCadeia(pontuacao, tabuleiro, linhas, colunas)
    exibeTabuleiro(tabuleiro)
    print(pontuacao)

main()