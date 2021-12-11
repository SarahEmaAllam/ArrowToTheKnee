from KnowledgeBase import KnowledgeBase
from Rule import Rule
from View.QuestionsHandler import QuestionsHandler
from View.MainWindow import *
import heapq
import copy
import math


# Method for reading lines from a .txt file and turning them into lists of strings
def read_knowledge():
    with open('knowledge_base.txt') as f:
        text = f.readlines()
    array = []
    # loop to remove newlines and to create individual entries for each word
    for line in text:
        line = str.strip(line)
        array.append(line.split(", "))
    return array


# Method for converting the lines read from a knowledge base to if-then rules
def convert_to_rules(knowledge):
    array = []
    for line in knowledge:
        rule = Rule()
        rule.set_diagnosis(line.pop())
        rule.set_count(int(line.pop()))
        rule.set_conclusion(line.pop())
        rule.set_premises(line)
        array.append(rule)
    return array


def retrieve_qustion_by_weight(missing_weights_in_rules):
    pass


def retrieve_question_by_premise(missing_premises_in_rules):
    pass


def solve_inference(patient, knowledge, fact, facts):
    missing_premises_in_rules = []
    for index, rule in enumerate(knowledge["rules"]):
        missing_premises = []
        for symptom in rule[0]:
            if symptom[0] is None: # symptom exists as premise
                missing_premises.append(symptom[0])
        missing_premises_in_rules.append((index, missing_premises)) # save nr of missing premises with the index of the rule
        
        missing_weights_in_rules = []
        if len(missing_premises) == 0: # no missing premises so we can do inference
            # check if the weights of the premises are higher than thresholds
            wrong_weights = []
            for weight in rule[0]:
                if weight[1] != True:  # not above threshold weight
                    # ask more questions
                    wrong_weights.append(weight[1])
            missing_weights_in_rules.append((index, wrong_weights))
            #if all weights are correct for a diagnosis
            if wrong_weights == 0:
                # infer a diagnosis and put it in the queue
                heapq.heappush(facts, rule[1])
            else:
                # there are wrong weights, next question should clarify the weight
                retrieve_qustion_by_weight(missing_weights_in_rules)
        else:
            # missing premises, next question should be about the missing premises
            retrieve_question_by_premise(missing_premises_in_rules)
                
                    




        # Method for comparing known facts to premises of rules
def satisfy_rules(patient, knowledge, fact, facts):
    for premise in knowledge["symptoms"]:
        if fact == premise[0]:
            solve_inference(patient, knowledge, fact, facts)

                # premise satisfied: "remove" premise from premise count
                # rule.set_count(rule.count - 1)
                # if rule.count == 0:
                    # check if conclusion is a diagnosis or another symptom
                #     if rule.diagnosis == "D":
                #         patient.add_diagnosis(rule.conclusion)
                #     else:
                #         patient.add_symptom(rule.conclusion)
                # break


def forward_chaining(window, patient):
    # read rules from file and convert to list of Rule objects
    # knowledge_base = read_knowledge()
    knowledge_base = KnowledgeBase()
    # knowledge_base = convert_to_rules(knowledge_base)

    obtained = patient.symptoms

    # TODO: move to the end of the algorithm (first question is generated before first fc call)
    # question = window.questions.pop()
    # window.update_window(question)

    #now send the question to the front end

    #get the premise from the answer
    # NOTE: window.sender() = the clicked button that lead to fc being called, symptom = symptom tied to button
    facts = []
    heapq.heappush(facts, window.sender().symptom)

    #the inference loop
    while len(facts)!= 0:

        #first update weight in co-variance matrix

        fact = heapq.heappop(facts) #pop by weight priority

        if fact not in patient.explored:
            patient.add_explored(fact)
            satisfy_rules(patient, knowledge_base.KB, fact, facts)



    # loop to match each obtained and not yet explored fact to rules in the knowledge base
    # for fact in obtained:
    #     if fact not in patient.explored:
    #         patient.add_explored(fact)
    #
    #         satisfy_rules(patient, knowledge_base, fact)

    print(patient.diagnoses, patient.symptoms)
