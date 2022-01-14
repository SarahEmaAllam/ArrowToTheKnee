from Model.Rule import Rule
from Model.Premise import Premise


class KnowledgeBase:

    def __init__(self):
        self.diagnoses = {
            # diagnosis 1
            'Enthesiopathy':
                {   'rules': [
                    # age variable: sets (value, weight)
                    ('1', 0),
                    ('2', 0.1),
                    ('3', 0.8),
                    ('4', 0),
                    ('5', 0.1),

                    # gender variable: sets (value, weight)
                    ('male', 0.8),
                    ('female', 0.2),

                    # symptoms start
                    ('gradual', 0.8),
                    ('sudden', 0.2),

                    # location pain: sets (value, weight)
                    ('front', 0),
                    ('inside', 0.1),
                    ('outside', 0.8),
                    ('back', 0),
                    ('within', 0.1),

                    # swelling knee
                    ('swelling', 1),
                    ('no_swelling', 0),
                    ('some_swell', 0),

                    # swelling location
                    ('local', 1),
                    ('whole_knee', 0),

                    # bend knee
                    ('bend_hurt', 0.8),
                    ('bend_ok', 0.2),

                    # bend knee pain
                    ('extend', 0.8),
                    ('bend', 0.2),
                    ('both', 0),

                    # activities hurt: sets (value, weight)
                    ('explosive', 0),
                    ('repeated', 0.2),
                    ('torsion', 0.8),
                    ('still', 0),

                ],
                    'activation': 0
                },

            'Patellofemoral painsyndrome':
                {'rules': [
                    # age variable: sets (value, weight)
                    ('1', 0.05),
                    ('2', 0.6),
                    ('3', 0.3),
                    ('4', 0.05),
                    ('5', 0),

                    # gender variable: sets (value, weight)
                    ('female', 0.7),
                    ('male', 0.3),


                    # symptoms start
                    ('gradual', 1),
                    ('sudden', 0),

                    # location pain: sets (value, weight)
                    ('front', 0.0),
                    ('inside', 0.1),
                    ('outside', 0),
                    ('back', 0),
                    ('within', 0),

                    # swelling knee
                    ('swelling', 0),
                    ('no_swelling', 0),
                    ('some_swell', 1),

                    # swelling location
                    ('local', 0),
                    ('whole_knee', 1),

                    # bend knee
                    ('bend_hurt', 1),
                    ('bend_ok', 0),

                    # bend knee pain
                    ('extend', 0),
                    ('bend', 1),
                    ('both', 0),

                    # activities hurt: sets (value, weight)
                    ('explosive', 1),
                    ('repeated', 1),
                    ('torsion', 1),
                    ('still', 0),


                ],
                    'activation': 0
                },

            'Osgood-Schlatter':
                {'rules': [
                    # age variable: sets (value, weight)
                    ('1', 0),
                    ('2', 1),
                    ('3', 0),
                    ('4', 0),
                    ('5', 0),

                    # gender variable: sets (value, weight)

                    ('female', 0.65),
                    ('male', 0.35),

                    # symptoms start
                    ('gradual', 1),
                    ('sudden', 0),

                    # location pain: sets (value, weight)
                    ('front', 0.9),
                    ('inside', 0),
                    ('outside', 0),
                    ('back', 0),
                    ('within', 0.1),

                    # swelling knee
                    ('swelling', 0),
                    ('no_swelling', 0),
                    ('some_swell', 1),

                    # swelling location
                    ('local', 1),
                    ('whole_knee', 0),

                    # bend knee
                    ('bend_hurt', 1),
                    ('bend_ok', 0),

                    # bend knee pain
                    ('extend', 1),
                    ('bend', 0),
                    ('both', 0),

                    # activities hurt: sets (value, weight)
                    ('explosive', 1),
                    ('repeated', 0.5),
                    ('torsion', 0),
                    ('still', 0.2),

                ],
                    'activation': 0
                },

            'Juvenile Osteochondritis':
                {'rules': [
                    # age variable: sets (value, weight)
                    ('1', 0),
                    ('2', 1),
                    ('3', 0),
                    ('4', 0),
                    ('5', 0),

                    # gender variable: sets (value, weight)

                    ('female', 0.45),
                    ('male', 0.45),

                    # symptoms start
                    ('gradual', 0.7),
                    ('sudden', 0.3),

                    # location pain: sets (value, weight)
                    ('front', 0),
                    ('inside', 0),
                    ('outside', 0),
                    ('back', 0),
                    ('within', 1),

                    # swelling knee
                    ('swelling', 1),
                    ('no_swelling', 0),
                    ('some_swell', 0),

                    # swelling location
                    ('local', 1),
                    ('whole_knee', 0),

                    # bend knee
                    ('bend_hurt', 0),
                    ('bend_ok', 1),

                    # bend knee pain
                    ('extend', 0),
                    ('bend', 0),
                    ('both', 1),

                    # activities hurt: sets (value, weight)
                    ('explosive', 1),
                    ('repeated', 0),
                    ('torsion', 1),
                    ('still', 0),

                ],
                    'activation': 0
                },


            'Iliotibial Band Syndrome':
                {'rules': [
                    # age variable: sets (value, weight)
                    ('1', 0),
                    ('2', 0),
                    ('3', 0.1),
                    ('4', 0.8),
                    ('5', 0.1),

                    # gender variable: sets (value, weight)

                    ('female', 0.8),
                    ('male', 0.2),

                    # symptoms start
                    ('gradual', 1),
                    ('sudden', 0),

                    # location pain: sets (value, weight)
                    ('front', 0),
                    ('inside', 0),
                    ('outside', 1),
                    ('back', 0),
                    ('within', 0),

                    # swelling knee
                    ('swelling', 0),
                    ('no_swelling', 0),
                    ('some_swell', 1),

                    # swelling location
                    ('local', 1),
                    ('whole_knee', 0),

                    # bend knee
                    ('bend_hurt', 1),
                    ('bend_ok', 0),

                    # bend knee pain
                    ('extend', 0),
                    ('bend', 0),
                    ('both', 1),

                    # activities hurt: sets (value, weight)
                    ('explosive', 0.9),
                    ('repeated', 0),
                    ('torsion', 0),
                    ('still', 0.1),

                ],
                    'activation': 0
                },


            'Knee arthritis':
                {'rules': [
                    # age variable: sets (value, weight)
                    ('1', 0),
                    ('2', 0),
                    ('3', 0),
                    ('4', 0),
                    ('5', 1),

                    # gender variable: sets (value, weight)

                    ('female', 0.55),
                    ('male', 0.45),

                    # symptoms start
                    ('gradual', 1),
                    ('sudden', 0),

                    # location pain: sets (value, weight)
                    ('front', 0),
                    ('inside', 0),
                    ('outside', 0),
                    ('back', 0),
                    ('within', 1),

                    # swelling knee
                    ('swelling', 1),
                    ('no_swelling', 0),
                    ('some_swell', 0),

                    # swelling location
                    ('local', 1),
                    ('whole_knee', 1),

                    # bend knee
                    ('bend_hurt', 1),
                    ('bend_ok', 0),

                    # bend knee pain
                    ('extend', 0),
                    ('bend', 0),
                    ('both', 1),

                    # activities hurt: sets (value, weight)
                    ('explosive', 0.3),
                    ('repeated', 0),
                    ('torsion', 0.7),
                    ('still', 0),

                ],
                    'activation': 0
                }

        }

# class KnowledgeBase:
#
#     def __init__(self):
#
#         # variables for symptoms
#
#         gender = 'gender'
#         age = 'age' # 5 categories
#         pain = None
#         middle_diagnosis=[1,0]
#         self.diagnoses = ['waffle', 'jerry']
#
#         # variables for weights
#         weight_gender = 0
#         weight_age = 0
#         weight_pain = 0
#         threshold = 0.8
#
#
#         self.KB = {}
#
#         self.symptoms = {
#             'age': None,
#             'gender': None,
#             'discomfortStart': None,
#             'painLocation': None,
#             'swollenKnee': None,
#             'swellPermanent': None,
#             'actionsHurt': None,
#             'movementsHurt': None
#         }
#             # (gender, weight_gender),
#             # (age, weight_age),
#             # (pain, weight_pain),
#
#
#         self.rules = [
#             ([
#                 (self.symptoms['gender'] == 'female', 1),
#                 (self.symptoms['age'] == '5', 1)
#             ],
#                 self.diagnoses[0]
#             ),
#             ]

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
