'''
The Knowledge Base holds the Diagnoses (rules), Questions and Treatments.
The diagnoses is comprised of value-weight pairs for each diagnosis.
'''

class KnowledgeBase:

    def __init__(self):
        self.diagnoses = {
            # diagnosis 1
            'Jumper\'s Knee':
                {'rules': [
                    # age variable: sets (value, weight)
                    ('1', 0),
                    ('2', 0.4),
                    ('3', 0.4),
                    ('4', 0.2),
                    ('5', 0),

                    # gender variable: sets (value, weight)
                    ('male', 0.6),
                    ('female', 0.4),

                    # symptoms start
                    ('gradual', 1),
                    ('sudden', 0),

                    # location pain: sets (value, weight)
                    ('front', 1),
                    ('inside', 0),
                    ('outside', 0),
                    ('back', 0),
                    ('within', 0),

                    # swelling knee
                    ('swelling', 0),
                    ('no_swelling', 0.85),
                    ('some_swell', 0.15),

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
                    ('explosive', 0.8),
                    ('repeated', 0.2),
                    ('torsion', 0),
                    ('still', 0.5),

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
                    ('front', 1),
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
                    ('1', 0.15),
                    ('2', 0.85),
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
                    ('1', -100),
                    ('2', 1),
                    ('3', -100),
                    ('4', -100),
                    ('5', -100),

                    # gender variable: sets (value, weight)

                    ('female', 0.45),
                    ('male', 0.55),

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


            'Knee Arthritis':
                {'rules': [
                    # age variable: sets (value, weight)
                    ('1', -100),
                    ('2', -100),
                    ('3', -100),
                    ('4', -100),
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

        self.questions = [["What is your age?",
                          [['0-12', '1'], ['12-18', '2'], ['18-30', '3'], ['30-55', '4'], ['55+', '5']],
                          'normal'],
                          ["What is your gender?",
                          [['Male', 'male'], ['Female', 'female']],
                          'normal'],
                          ["How did the pain start?",
                          [['Gradually', "gradual"], ['Suddenly', 'sudden']],
                          'normal'],
                          ["Where is the pain located?",
                          [['Front', 'front'], ['Inner Side', 'inside'], ['Outer Side', 'outside'],
                           ['Backside', 'back'], ['Within', 'within']],
                          'normal'],
                          ["Is there swelling of the knee?",
                          [['Yes', 'swelling'], ['No', 'no_swelling'], ['Sometimes', 'some_swell']],
                          'normal'],
                          ["Where is the swelling located?",
                          [['In one spot', 'local'], ['Whole Knee', 'whole_knee']], 'normal'],
                          ["Does bending or extending the knee hurt?", [['Yes', 'bend_hurt'], ['No', 'bend_ok']],
                          'normal'],
                          ["Which of the following movements hurts the most?",
                          [['Extending the knee', 'extend'], ['Bending the knee', 'bend'], ['Both', 'both']],
                          'normal'],
                          ["Which of the following movements hurt?\n(Left = no pain, Right = extreme pain)",
                           [['Explosive Movements', 'explosive'], ['Repeated Movements', 'repeated'],
                            ['Movement with torsions', 'torsion'], ['Sitting still', 'still']],
                           'multi']
                          ]

        self.treatments = {
            'Jumper\'s Knee': "Reduce the load on your knee relative to your usual strength.\nAvoid jumping and peak "
                              "exercises until the pain subsides.\nIf the pain returns, lower your overall physical "
                              "load.\nTrain your upper leg and hip stabilizers with alternating leg movements\n(avoid "
                              "double leg exercises such as squats).\nEstimated time until recovery: 6-12 months.",

            'Patellofemoral painsyndrome': "Train your upper leg and hip stabilizers, if needed with the help of a "
                                           "physiotherapist.\nThe syndrome is painful, but not dangerous otherwise.\n"
                                           "Estimated time until recovery: 3-5 months",

            'Osgood-Schlatter': "Reduce the load on your knee relative to the amount of pain you are experiencing\n"
                                "That is, if you are experiencing more pain, take it easier. It disappears on its own.",

            'Juvenile Osteochondritis': "Severity is to be examined through an MRI scan.\nIf it is not severe, "
                                        "train the upper leg and butt muscles\nwith alternating leg movements (avoid "
                                        "double leg exercises such as squats).\nKeep training as long as the issue "
                                        "persists. ",

            'Iliotibial Band Syndrome': "Train the leg muscles one leg at a time.\nSupplement with stretches to lessen "
                                        "the pain.\nEstimated time until recovery: 3-5 months.",

            'Knee Arthritis': "Knee Arthritis never goes away completely.\nIt is essential to keep exercising the "
                              "legs. Practice walking and cycling.\nAvoid swimming, as the movement of the leg is "
                              "harder to control."
            }
