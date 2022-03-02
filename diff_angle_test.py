from utils import *

import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))

    CENTER = (200, 200)
    RADIUS = 100

    dot_a = (CENTER[0]+RADIUS, CENTER[1])
    dot_a_color = (243, 79, 79)
    dot_b = (CENTER[0], CENTER[1]-RADIUS)
    dot_b_color = (243, 243, 79)

    screen.fill((152, 206, 231))
    pygame.draw.circle(screen, (71, 153, 192), CENTER, RADIUS)

    pygame.draw.circle(screen, dot_a_color, dot_a, 16)
    pygame.draw.line(screen, dot_a_color, CENTER, dot_a, 10)
    pygame.draw.circle(screen, dot_b_color, dot_b, 16)
    pygame.draw.line(screen, dot_b_color, CENTER, dot_b, 10)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            state = pygame.mouse.get_pressed()
            if (state[0]):
                mouse = pygame.mouse.get_pos()
                vector = (mouse[0]-CENTER[0], mouse[1]-CENTER[1])
                distance = (vector[0]**2 + vector[1]**2)**0.5

                if distance > 0:
                    scalar = RADIUS / distance

                    click_color = screen.get_at(pygame.mouse.get_pos())

                    if click_color == dot_a_color:
                        dot_a = (
                            int(round(CENTER[0] + vector[0]*scalar)),
                            int(round(CENTER[1] + vector[1]*scalar)))
                    elif click_color == dot_b_color:
                        dot_b = (
                            int(round(CENTER[0] + vector[0]*scalar)),
                            int(round(CENTER[1] + vector[1]*scalar)))

                screen.fill((152, 206, 231))
                pygame.draw.circle(screen, (71, 153, 192), CENTER, RADIUS)
                pygame.draw.circle(screen, dot_a_color, dot_a, 16)
                pygame.draw.line(screen, dot_a_color, CENTER, dot_a, 10)
                pygame.draw.circle(screen, dot_b_color, dot_b, 16)
                pygame.draw.line(screen, dot_b_color, CENTER, dot_b, 10)

        pygame.display.update()


if __name__ == "__main__":
    main()
