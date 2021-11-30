from .Rule import Rule


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


# Method for comparing known facts to premises of rules
def satisfy_rules(patient, knowledge, fact):
    for rule in knowledge:
        for premise in rule.premises:
            if fact == premise:
                # premise satisfied: "remove" premise from premise count
                rule.set_count(rule.count - 1)
                if rule.count == 0:
                    # check if conclusion is a diagnosis or another symptom
                    if rule.diagnosis == "D":
                        patient.add_diagnosis(rule.conclusion)
                    else:
                        patient.add_symptom(rule.conclusion)
                break


def forward_chaining(patient):
    # read rules from file and convert to list of Rule objects
    knowledge_base = read_knowledge()
    knowledge_base = convert_to_rules(knowledge_base)

    obtained = patient.symptoms

    # loop to match each obtained and not yet explored fact to rules in the knowledge base
    for fact in obtained:
        if fact not in patient.explored:
            patient.add_explored(fact)

            satisfy_rules(patient, knowledge_base, fact)

    print(patient.diagnoses, patient.symptoms)
