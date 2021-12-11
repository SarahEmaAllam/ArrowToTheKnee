from Premise import Premise


class Rule(object):
    def __init__(self, premises=[]):
        self.premises = premises
        self.conclusion = ""
        self.count = 0
        self.diagnosis = ""

    def add_premise(self, premise):
        self.premises.append(premise)

    def set_conclusion(self, conclusion):
        self.conclusion = conclusion

    def set_count(self, count):
        self.count = count

    def set_diagnosis(self, diagnosis):
        self.diagnosis = diagnosis

        #todo DECOUPLE PREMISE FROM RULE. MULTIPLE RULES CAN HAVE THE SAME PREMISE. EVERY PREMISE HAS A WEIGHT
        # attempted this with class Premise but idk if it's what you envisioned