import json
import random

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question.prompt)
        for index, option in enumerate(question.options, start=1):
            print(f"{index}. {option}")

    def load_questions_from_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            for item in data:
                question = Question(item["prompt"], item["options"], item["answer"])
                self.questions.append(question)

    def run_quiz(self):
        random.shuffle(self.questions)
        for question in self.questions:
            self.display_question(question)
            user_answer = input("Enter your answer (1, 2, 3, ...): ")
            if user_answer.isdigit():
                index = int(user_answer) - 1
                if 0 <= index < len(question.options):
                    if question.options[index] == question.answer:
                        print("Correct!")
                        self.score += 1
                    else:
                        print("Incorrect!")
                else:
                    print("Invalid option!")
            else:
                print("Invalid input!")
        print(f"Quiz completed! Your score: {self.score}/{len(self.questions)}")

# Example usage
questions = []
quiz = Quiz(questions)
quiz.load_questions_from_file("questions.json")  # Load questions from a JSON file
quiz.run_quiz()
