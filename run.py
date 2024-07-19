import random

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

def run_quiz(questions):
    score = 0
    incorrect_questions = []

    random.shuffle(questions)

    for question in questions:
        print(question.prompt)
        for i, option in enumerate(question.options):
            print(f"{i + 1}. {option}")
        try:
            answer = int(input("Enter the number of the correct answer: "))
            if question.options[answer - 1] == question.answer:
                score += 1
            else:
                incorrect_questions.append((question, answer))
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number corresponding to one of the options.")
            incorrect_questions.append((question, None))
    
   