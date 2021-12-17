from View.Button import Button
from View.Question import Question
import heapq

# this class should handle all the existing questions :
# it retrieves the next question base don the KB priority
# it stashes already explored questions


class QuestionsHandler:
    def __init__(self, kb):
        self.questions = self.initialize_questions(kb)
        print(self.questions)
        self.explored = []

    def add_question(self, question):
        self.questions.append(question)

    # Currently not used
    def question1(self, text, variable, button1, symp1, button2, symp2):
        question = Question(text)
        question.variable = variable
        self.add_question(question)
        question.create_button(button1, symp1)
        question.create_button(button2, symp2)

    # Method for reading questions from a .txt file and processing them into Question objects
    def initialize_questions(self, kb):
        with open('questions.txt') as f:
            text = f.readlines()
        array = []
        # loop to remove newlines and to create individual entries for each item
        for line in text:
            line = str.strip(line)
            array.append(line.split("_"))
        print(array)

        questions = []
        for line in array:
            question = Question()
            question.question = line.pop(0)
            print(question.question)
            variable = line.pop(0)
            print(variable)
            question.variable = variable
            print(question.variable)
            while len(line) != 0:
                question.create_button(line.pop(), line.pop())

            questions.append(question)

        for question in questions:
            print(question.question)
        print("a")
        return questions

    # Method for adding a question to the questions we've explored
    def add_explored(self, question):
        self.explored.append(question)
