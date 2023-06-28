import pygame

def play():
    pygame.init()

    def game(clock):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            pygame.display.update()
            clock.tick(FPS)

    clock = pygame.time.Clock()
    FPS = 50
    pygame.display.set_mode((400, 600))
    pygame.display.set_caption("GEM GAME")

    game(clock)
    pygame.quit()