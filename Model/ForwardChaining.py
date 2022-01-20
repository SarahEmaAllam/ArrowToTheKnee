import heapq
'''
This function is the inference model. This is the main loop that applies the rules from the KB
to the new answer given by the user and retrieves the maximum diagnosis score back to the UI
'''


def forward_chaining(window, knowledge_base, symptoms):

    facts = []
    explored = []
    heapq.heappush(facts, symptoms)

    while len(facts) > 0:

        fact = heapq.heappop(facts[0])  # pop by weight priority
        scale = 0

        if type(fact) == list and len(fact) > 0:

            scale = fact[1]
            fact = fact[0]

        scores = {}

        if fact not in explored:
            explored.append(fact)

            for diagnosis in knowledge_base.diagnoses:
                for rule in knowledge_base.diagnoses[diagnosis]['rules']:
                    premise = rule[0]
                    weight = rule[1]
                    if fact == premise:
                        if scale != 0:
                            weight = (weight * float(scale))/5

                        knowledge_base.diagnoses[diagnosis]['activation'] += weight
                        scores[diagnosis] = knowledge_base.diagnoses[diagnosis]['activation']

            return max(scores, key=scores.get)
