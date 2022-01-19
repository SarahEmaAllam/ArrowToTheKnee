'''
The patient class keeps track of the answers that the user gave:
this is the data that has been sent to the rules to produce new data
'''
class Patient(object):
    def __init__(self, symptoms=[], diagnoses=[], explored=[]):
        self.symptoms = symptoms
        self.diagnoses = diagnoses
        self.explored = explored

    def add_symptom(self, symptom):
        self.symptoms.append(symptom)

    def add_diagnosis(self, diagnosis):
        self.diagnoses.append(diagnosis)

    def add_explored(self, explored):
        self.explored.append(explored)
