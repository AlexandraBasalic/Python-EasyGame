import pygame
from quiz_game import run_quiz

if __name__ == "__main__":
    run_quiz()


pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Python Game")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
