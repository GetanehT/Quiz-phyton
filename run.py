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
    
    print(f"\nYou got {score} out of {len(questions)} correct!")
    
    if incorrect_questions:
        print("\nHere are the questions you answered incorrectly:")
        for question, given_answer in incorrect_questions:
            print(f"\nQuestion: {question.prompt}")
            print(f"Your answer: {given_answer if given_answer is not None else 'Invalid input'}")
            print(f"Correct answer: {question.answer}")

#Sample questions

questions = [
    Question( 
        
        "Which planet is known as the Red Planet?",
           ["Earth", "Mars", "Jupiter", "Venus"],
         "Mars"
    ),
  
     
  Question( 
        
        "What is the capital of France?",
         ["Berlin", "Madrid", "Paris", "Lisbon"],
          "Paris"
    ),
   Question( 
        
        "What is the capital of France?",
         ["Berlin", "Madrid", "Paris", "Lisbon"],
          "Paris"
    ),
  Question( 
        
        "What is the capital of France?",
         ["Berlin", "Madrid", "Paris", "Lisbon"],
          "Paris"
    ),
  Question( 
        
        "What is the capital of France?",
         ["Berlin", "Madrid", "Paris", "Lisbon"],
          "Paris"
    )

]

run_quiz(questions)