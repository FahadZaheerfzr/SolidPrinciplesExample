'''
    This is an example of a class that violates the Open Closed Principle.
    If we need to add a new question type, we need to modify the class.
'''
class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def take_quiz(self):
        for question in self.questions:
            print(question["text"])
            if question["type"] == "multiple choice":
                for choice in question["choices"]:
                    print(str(question["choices"].index(choice)) + ". " + choice)

            if question["type"] == "boolean":
                print("0. True")
                print("1. False")

            if question["type"] == "text":
                print("Enter your answer: __________")

            print()


questions = [
    {
        "text": "What is the capital of France?",
        "type": "multiple choice",
        "choices": ["Paris", "London", "Berlin", "Rome"]
    },
    {
        "text": "Is the sky blue?",
        "type": "boolean"
    },
    {
        "text": "What is the square root of 100?",
        "type": "text"
    }
]

quiz = Quiz(questions)
quiz.take_quiz()