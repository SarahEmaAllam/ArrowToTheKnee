from View.Button import Button
from View.Question import Question
import heapq

# this class should handle all the existing questions :
# it retrieves the next question base don the KB priority
# it stashes already explored questions


class QuestionsHandler:
    def __init__(self):
        self.questions = self.initialize_questions()
        self.explored = []

    def add_question(self, question):
        self.questions.append(question)

    def question1(self, text, button1, symp1, button2, symp2):
        question = Question(text)
        self.add_question(question)
        question.create_button(button1, symp1)
        question.create_button(button2, symp2)

    def initialize_questions(self):
        with open('questions.txt') as f:
            text = f.readlines()
        array = []
        # loop to remove newlines and to create individual entries for each word
        for line in text:
            line = str.strip(line)
            array.append(line.split(","))

        questions = []
        for line in array:
            question = Question()
            question.set_weight(float(line.pop()))
            count = len(line)
            while count != 1:
                question.create_button(line.pop(), line.pop())
                count -= 2
            question.set_question(line.pop())
            heapq.heappush(questions, question)

        return questions

    def pop(self):
        priority = 0
        for i in range(len(self.questions)):
            if self.questions[i].weight > self.questions[priority].weight:
                priority = i
        item = self.questions[priority]
        del self.questions[priority]
        self.add_explored(item)
        return item

    def add_explored(self, question):
        self.explored.append(question)
