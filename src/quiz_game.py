import json
import random
import os
import pygame


def load_questions(filename):
    base_path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(base_path, '..', filename)
    print(f"Looking for file at: {filepath}")
    with open(filepath, 'r') as file:
        return json.load(file)


def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def ask_question(screen, question, font):
    screen.fill((0, 0, 0))
    draw_text(screen, question['question'], font, (255, 255, 255), 20, 20)
    for i, option in enumerate(question['options']):
        draw_text(screen, f"{i + 1}. {option}", font, (255, 255, 255), 20, 60 + i * 40)
    pygame.display.flip()


def run_quiz(screen, font):
    questions = load_questions('questions.json')
    random.shuffle(questions)
    score = 0
    current_question = 0
    total_questions = len(questions)

    while current_question < total_questions:
        ask_question(screen, questions[current_question], font)
        waiting_for_answer = True

        while waiting_for_answer:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        answer = 0
                    elif event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        answer = 1
                    elif event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        answer = 2
                    elif event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        answer = 3
                    else:
                        continue

                    if questions[current_question]['options'][answer] == questions[current_question]['answer']:
                        score += 1
                        print("Correct!")
                    else:
                        print(f"Wrong! The correct answer was {questions[current_question]['answer']}.")

                    waiting_for_answer = False
                    current_question += 1

    print(f"Your final score: {score}/{total_questions}")
