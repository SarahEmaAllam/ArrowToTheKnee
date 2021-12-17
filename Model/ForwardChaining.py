from KnowledgeBase import KnowledgeBase
from Rule import Rule
from View.QuestionsHandler import QuestionsHandler
from View.MainWindow import *
import heapq
import copy
import math

flag = False
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


def retrieve_question_by_premise(missing_premises_in_rules, window):
    question = window.questions.pop()
    window.updateWindow(question)


def solve_inference(patient, knowledge, fact, facts, window):
    missing_premises_in_rules = []
    for index, rule in enumerate(knowledge.rules):
        print("rule is with index", rule, index)
        missing_premises = []
        for symptom in rule[0]:
            print("symptom in rule is ", symptom)
            if symptom[0] is None: # symptom exists as premise
                print("missing symptom is ", symptom[0])
                missing_premises.append(symptom[0])
        missing_premises_in_rules.append((index, missing_premises))  # save nr of missing premises with the index of the rule
        
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
                flag = rule[1]
                print("Your diagnosis is ", rule[1])
                exit(0)
            # else:
            #     # there are wrong weights, next question should clarify the weight
            #     retrieve_qustion_by_weight(missing_weights_in_rules, window)
        else:
            # missing premises, next question should be about the missing premises
            retrieve_question_by_premise(missing_premises_in_rules, window)
                
                    




        # Method for comparing known facts to premises of rules
def satisfy_rules(patient, knowledge, fact, facts, window):
    for premise in knowledge.symptoms:
        print("premise in KB is ", premise, knowledge.symptoms[premise])
        if fact == knowledge.symptoms[premise]:
            print("fact is equal to premise[0] symptom ", fact, knowledge.symptoms[premise])
            solve_inference(patient, knowledge, fact, facts, window)

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
    knowledge_base = window.kb
    # knowledge_base = convert_to_rules(knowledge_base)

    # TODO: move to the end of the algorithm (first question is generated before first fc call)
    # question = window.questions.pop()
    # window.update_window(question)

    #get the premise from the answer
    # NOTE: window.sender() = the clicked button that lead to fc being called, symptom = symptom tied to button
    facts = []
    heapq.heappush(facts, window.sender().symptom)


    #the inference loop
    while len(facts) < 0:

        #first update weight in co-variance matrix

        fact = heapq.heappop(facts) #pop by weight priority
        print("fact popped is ", fact)

        if fact not in patient.explored:
            patient.add_explored(fact)
            satisfy_rules(patient, knowledge_base, fact, facts, window)



    # loop to match each obtained and not yet explored fact to rules in the knowledge base
    # for fact in obtained:
    #     if fact not in patient.explored:
    #         patient.add_explored(fact)
    #
    #         satisfy_rules(patient, knowledge_base, fact)

    print(knowledge_base.diagnoses, patient.symptoms)
    print("print questions", len(window.questions.questions), window.questions.questions)
    if len(window.questions.questions) != 0:
        window.update_window(window.questions.questions.pop(), patient)



