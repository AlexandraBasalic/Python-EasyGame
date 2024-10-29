import pygame
from quiz_game import run_quiz

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Game")
font = pygame.font.Font(None, 36)

if __name__ == "__main__":
    run_quiz(screen, font)

pygame.quit()
