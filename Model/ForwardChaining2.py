from KnowledgeBase import KnowledgeBase
from Rule import Rule
from View.QuestionsHandler import QuestionsHandler
from View.MainWindow import *
import heapq
import copy
import math

def forward_chaining(window, knowledge_base, symptoms):

    facts = []
    explored = []
    heapq.heappush(facts, symptoms)
    # heapq.heappush(facts, symptom)

    print("current fact is now in FC:", facts)

    while len(facts) > 0:

        fact = heapq.heappop(facts[0])  # pop by weight priority
        print(type(fact))
        if type(fact) == list and len(fact) >0:
            fact = fact[0]
        print("fact popped is ", fact)
        scores = {}

        if fact not in explored:
            explored.append(fact)

            for diagnosis in knowledge_base.diagnoses:
                print('diagnosis ', diagnosis)
                for rule in knowledge_base.diagnoses[diagnosis]['rules']:
                    premise = rule[0]
                    weight = rule[1]
                    if fact == premise:
                        print(fact, 'and ', premise, 'are equal')
                        print('before actibvation sum', knowledge_base.diagnoses[diagnosis]['activation'])
                        knowledge_base.diagnoses[diagnosis]['activation'] += weight
                        print(' now activation is ', knowledge_base.diagnoses[diagnosis]['activation'])
                        scores[diagnosis] = knowledge_base.diagnoses[diagnosis]['activation']
                        # scores.append(knowledge_base.diagnoses[diagnosis]['activation'])

            print('scores', scores)
            print("=======score======", max(scores, key=scores.get))
            return max(scores, key=scores.get)
