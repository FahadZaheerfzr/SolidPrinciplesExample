'''
    This is an example of a class that follows the Open Closed Principle.
    If we need to add a new question type, we can do so without modifying 
    the class Quiz by writing a new class for that question.
'''

class Quiz:
    def __init__(self, questions):
        self.questions = questions

    def take_quiz(self):
        for question in self.questions:
            question.printQuestionChoices()
            print()

class BooleanQuestion:
    def __init__(self, description):
        self.description = description

    def printQuestionChoices(self):
        print(self.description)
        print("0. True")
        print("1. False")


class MultipleChoiceQuestion:
    def __init__(self, description, choices):
        self.description = description
        self.choices = choices

    def printQuestionChoices(self):
        print(self.description)
        for choice in self.choices:
            print(str(self.choices.index(choice)) + ". " + choice)


class TextQuestion:
    def __init__(self, description):
        self.description = description

    def printQuestionChoices(self):
        print(self.description)
        print("Enter your answer: __________")


class RangeQuestion:
    def __init__(self, description, min, max):
        self.description = description
        self.min = min
        self.max = max

    def printQuestionChoices(self):
        print(self.description)
        print("Enter a number between " + str(self.min) + " and " + str(self.max))


questions = [
    MultipleChoiceQuestion("What is the capital of France?", ["Paris", "London", "Berlin", "Rome"]),
    BooleanQuestion("Is the sky blue?"),
    TextQuestion("What is the square root of 100?"),
    RangeQuestion("What is the square root of 100?", 0, 100)
]

quiz = Quiz(questions)
quiz.take_quiz()