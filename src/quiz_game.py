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

def draw_text(screen, text, font, color, x, y, center=False):
    text_surface = font.render(text, True, color)
    if center:
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)
    else:
        screen.blit(text_surface, (x, y))

def ask_question(screen, question, font, font_path, watermark_image):
    screen.fill((245, 222, 179))  # Light beige background color

    # Draw watermark image
    watermark_rect = watermark_image.get_rect(center=(400, 500))
    screen.blit(watermark_image, watermark_rect)

    # Shuffle the options
    options = question['options']
    random.shuffle(options)

    draw_text(screen, question['question'], font, (101, 67, 33), 400, 100, center=True)  # Dark brown text color
    for i, option in enumerate(options):
        draw_text(screen, f"{i + 1}. {option}", font, (101, 67, 33), 400, 160 + i * 30, center=True)  # Adjust spacing
    pygame.display.flip()

    return options.index(question['answer'])  # Return the new index of the correct answer

def show_feedback(screen, font, message, watermark_image):
    screen.fill((245, 222, 179))  # Light beige background color

    # Draw watermark image
    watermark_rect = watermark_image.get_rect(center=(400, 500))
    screen.blit(watermark_image, watermark_rect)

    draw_text(screen, message, font, (101, 67, 33), 400, 300, center=True)  # Dark brown text color
    pygame.display.flip()
    pygame.time.delay(2000)  # Pause for 2 seconds to show feedback

def run_quiz(screen, font, font_path):
    questions = load_questions('questions.json')
    random.shuffle(questions)
    score = 0
    current_question = 0
    total_questions = len(questions)

    # Load the watermark image
    watermark_image = pygame.image.load(os.path.join(os.path.dirname(__file__), 'watermark.png')).convert_alpha()

    while current_question < total_questions:
        correct_answer_index = ask_question(screen, questions[current_question], font, font_path, watermark_image)
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

                    if answer == correct_answer_index:
                        score += 1
                        show_feedback(screen, font, "Correct!", watermark_image)
                    else:
                        show_feedback(screen, font, f"Wrong! The correct answer was {questions[current_question]['answer']}.", watermark_image)

                    waiting_for_answer = False
                    current_question += 1

    show_feedback(screen, font, f"Your final score: {score}/{total_questions}", watermark_image)
