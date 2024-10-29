import pygame
from quiz_game import run_quiz
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Quiz Game")

# Set custom window icon
icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)

# Load the pixelated font
font_path = 'src/PressStart2P-Regular.ttf'  # Update this path to your font file
font = pygame.font.Font(font_path, 16)  # Smaller font size

if __name__ == "__main__":
    run_quiz(screen, font, font_path)

pygame.quit()
