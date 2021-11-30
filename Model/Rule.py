
class Rule(object):
    def __init__(self):
        self.premises = []
        self.conclusion = ""
        self.count = 0
        self.diagnosis = ""

    def set_premises(self, premises):
        self.premises = premises

    def set_conclusion(self, conclusion):
        self.conclusion = conclusion

    def set_count(self, count):
        self.count = count

    def set_diagnosis(self, diagnosis):
        self.diagnosis = diagnosis
