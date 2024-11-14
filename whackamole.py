import pygame
import random

# Martina Delger Whack-a-mole

def draw_grid():
    # pygame.draw.line(screen, color, (x1, y1), (x2, y2))
    #draw horizontal lines
    for i in range(1, board_rows):
        pygame.draw.line(
            screen,
            line_color,
            (0, i*square_size),
            (640, i*square_size)
        )
    #draw vertical lines
    for i in range(1, board_cols):
        pygame.draw.line(
            screen,
            line_color,
            (i*square_size, 0),
            (i*square_size, 512)
        )

line_color = (0, 0, 0)
screen = pygame.display.set_mode((640, 512))
board_rows = 16
board_cols = 20
square_size = 32
mole_x = 0
mole_y = 0

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(0,0)))
        mole_image = pygame.image.load("mole.png")
        # screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        screen.fill("light pink")
        draw_grid()
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        pygame.display.flip()
        clock.tick(60)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mole_y = random.randrange(0, board_rows)
                    mole_x = random.randrange(0, board_cols)
                    # print(x,y)
                    screen.fill("light pink")
                    draw_grid()
                    screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x*square_size, mole_y*square_size)))
                    pygame.display.flip()

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
