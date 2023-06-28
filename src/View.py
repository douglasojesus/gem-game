import pygame

pygame.init()

# Define as cores das gemas
GEM_COLORS = {
    "A": (255, 0, 0),    # Vermelho
    "B": (0, 255, 0),    # Verde
    "C": (0, 0, 255),    # Azul
    "D": (255, 255, 0)  # Amarelo
}

# Define as dimessões da tela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

FPS = 50
FONT = pygame.font.SysFont("arialblack", 14)
CLOCK = pygame.time.Clock()
screen = pygame.display.set_mode((400, 600))
screen.fill("gray")
pygame.display.set_caption("GEM GAME")

def drawText(screen, text, font, textColor, posx, posy):
    img = font.render(text, True, textColor)
    screen.blit(img, (posx, posy))

def draw_gem_table(tabuleiro, TABLE_COLS, TABLE_ROWS, cell_width, cell_height):
    margemHorizontal = 40
    margemVertical = 40
    for row in range(TABLE_ROWS):
        for col in range(TABLE_COLS):
            # Calcule as coordenadas da célula
            x = margemHorizontal
            y = margemVertical
            margemHorizontal += 40
            # Obtenha o valor da gema na matriz
            gem_value = tabuleiro[row][col]
            # Obtenha a cor correspondente à gema
            gem_color = GEM_COLORS[gem_value]
            # Desenhe a célula circular
            radius = 20
            pygame.draw.circle(screen, gem_color, (x, y), radius)
        margemVertical += 40
        margemHorizontal = 40

def play(tabuleiro, TABLE_COLS, TABLE_ROWS):
    # Calcula as dimensões das células da tabela
    cell_width = (SCREEN_WIDTH-100) // TABLE_COLS
    cell_height = (SCREEN_HEIGHT-100) // TABLE_ROWS
    spaceNotPressed = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    spaceNotPressed = False
        screen.fill("gray")  # Limpa a tela a cada iteração
        if spaceNotPressed:
            drawText(screen, "O jogo vai começar! Aperte a tecla espaço.", FONT, (0, 0, 0), 20, 20)
        else:
            draw_gem_table(tabuleiro, TABLE_COLS, TABLE_ROWS, cell_width, cell_height)
        pygame.display.flip()
        CLOCK.tick(FPS)
        pygame.display.update()