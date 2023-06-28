import pygame

# Defina as dimensões da tela e da tabela
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TABLE_ROWS = 8
TABLE_COLS = 8

# Defina as cores das gemas
GEM_COLORS = [
    (255, 0, 0),    # Vermelho
    (0, 255, 0),    # Verde
    (0, 0, 255),    # Azul
    (255, 255, 0),  # Amarelo
    (255, 0, 255),  # Magenta
    (0, 255, 255)   # Ciano
]

# Inicialize o Pygame
pygame.init()

# Crie a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Gem Game")

# Calcule as dimensões das células da tabela
cell_width = SCREEN_WIDTH // TABLE_COLS
cell_height = SCREEN_HEIGHT // TABLE_ROWS

# Crie uma matriz de exemplo
gem_matrix = [
    [1, 2, 3, 4, 5, 0, 0, 0],
    [2, 3, 4, 5, 1, 0, 0, 0],
    [3, 4, 5, 1, 2, 0, 0, 0],
    [4, 5, 1, 2, 3, 0, 0, 0],
    [5, 1, 2, 3, 4, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

def draw_gem_table():
    for row in range(TABLE_ROWS):
        for col in range(TABLE_COLS):
            # Calcule as coordenadas da célula
            x = col * cell_width
            y = row * cell_height

            # Obtenha o valor da gema na matriz
            gem_value = gem_matrix[row][col]

            # Obtenha a cor correspondente à gema
            gem_color = GEM_COLORS[gem_value]

            # Desenhe a célula circular
            radius = 5
            pygame.draw.circle(screen, gem_color, (x, y), radius)

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Preencha a tela com a cor branca

    # Desenhe a tabela de gemas
    draw_gem_table()

    pygame.display.flip()

# Encerre o Pygame
pygame.quit()
