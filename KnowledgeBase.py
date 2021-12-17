from Model.Rule import Rule
from Model.Premise import Premise


class KnowledgeBase:

    def __init__(self):

        # variables for symptoms

        gender = 'gender'
        age = 'age' # 5 categories
        pain = None
        middle_diagnosis=[1,0]
        self.diagnoses = ['waffle', 'jerry']

        # variables for weights
        weight_gender = 0
        weight_age = 0
        weight_pain = 0
        threshold = 0.8


        self.KB = {}

        self.symptoms = {
            'age': None,
            'gender': None,
            'discomfortStart': None,
            'painLocation': None,
            'swollenKnee': None,
            'swellPermanent': None,
            'actionsHurt': None,
            'movementsHurt': None
        }
            # (gender, weight_gender),
            # (age, weight_age),
            # (pain, weight_pain),


        self.rules = [
            ([
                (self.symptoms['gender'] == 'female', 1),
                (self.symptoms['age'] == '5', 1)
            ],
                self.diagnoses[0]
            ),
            ]

    # def Enthesiopathy(self):
        # for index, symptom in enumerate(self.symptoms):



            # ([
            #     # all premises have to be present and to return 1 (true)
            #     (gender == 1, weight_gender >= 0.70),  # parameter is a variable converted to 0 or 1 boolean and then given a weight
            #     (age == 2, weight_age >= 0.30),
            #     (pain == 3, weight_pain >= 0.50),
            #     ((weight_pain+weight_age+weight_gender)/3 >= threshold)  # calculate the average probability of all symptoms
            # ],
            #  middle_diagnosis[0]  # diagnosis is the second parameter in the symptoms-diagnosis set
            # ),
            # # rule 2 and so on ....
            # (middle_diagnosis == 1, diagnoses[0])
        # ]

        # self.KB["rules"] = [(["croak", "sings"], "frog"),  # ([premise1, premise2], conclusion)  -> all conjunctions
        #                     (["sings", "yellow"], "bird"),
        #                     (["talks", "walks"], "human"),
        #                     (["frog"], "swims"),
        #                     (["bird"], "flies")
        #                     ]
        #
        # self.KB["symptoms"] = [("croak", "tim"), ("sings", "tim"),
        #                        ("talks", "maria"),
        #                        ("yellow", "tom"), ("sings", "tom"),
        #                        ("bird", "nick")]
        #
        # self.KB["diagnoses"] = ["tim", "tom", "maria", "nick"]
