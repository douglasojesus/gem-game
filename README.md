<h1 align="center">
📄<br>Jogo de gemas
</h1>
<h4 align="center">
Projeto criado usando como inspiração a atividade do M.I de Algoritmos e Programação (2023.1).
</h4>

O jogo Gemas consiste em um tabuleiro com m colunas e n linhas contendo gemas de c cores distintas. A cada passo do jogo, o jogador ou jogadora deve permutar de posição duas gemas adjacentes de tal forma que se crie uma cadeia de 3 ou mais gemas da mesma cor. Quando tal cadeia é criada, as gemas correspondentes são destruídas (eliminadas), gerando pontos para o jogador (igual ao número de gemas destruídas) e fazendo com que as gemas que se encontram acima “caiam”, tomando o lugar das gemas destruídas. Ao cair, é possível que novas cadeias se formem, causando uma reação em cadeia. Os espaços vazios criados pelas gemas que caíram são então preenchidos por gemas geradas aleatoriamente. Esse passo também pode criar novas cadeias que são automaticamente eliminadas, reiniciando o ciclo.
Duas gemas são consideradas adjacentes se elas se encontram na mesma linha e em colunas adjacentes, ou se elas se encontram na mesma coluna e em linhas adjacentes (diagonais não fazem parte da adjacência).
O jogo termina quando não existem permutações que geram cadeias. 

Tabuleiro e gemas
O tabuleiro deve ser representado por uma matriz m x n de strings, onde m e n são fornecidos pelo usuário. Cada tipo (cor) de gema é representado por uma letra maiúscula distinta, utilizando-se das c primeiras letras do alfabeto em caixa alta (A, B, C, …). Você pode assumir que o número de colunas e linhas é no máximo 10.
