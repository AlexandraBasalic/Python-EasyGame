import json
import random

def load_questions(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def ask_question(question):
    print(f"Question: {question['question']}")
    for i, option in enumerate(question['options']):
        print(f"{i + 1}. {option}")
    answer = int(input("Your answer (1-4): ")) - 1
    return question['options'][answer] == question['answer']

def run_quiz():
    questions = load_questions('src/questions.json')
    random.shuffle(questions)
    score = 0

    for question in questions:
        if ask_question(question):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {question['answer']}.")

    print(f"Your final score: {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()
