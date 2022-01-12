from PySide2.QtWidgets import QStackedWidget
from View.Window import *
from View.IntroductionWindow import *

questions = {'age_question': ["What is your age?",
                              [['0-12', '1'], ['12-18', '2'], ['18-39', '3'], ['39-55', '4'], ['55+', '5']],
                              'normal'],
             'gender_question': ["What is your gender?",
                                 [['Male', 'male'], ['Female', 'female']],
                                 'normal'],
             'pain_start_question': ["How did the pain start?",
                                     [['Gradually', "gradual"], ['Suddenly', 'sudden']],
                                     'normal'],
             'pain_location_question': ["Where is the pain located?",
                                        [['Front', 'front'], ['Inner Side', 'inside'], ['Outer Side', 'outside'],
                                         ['Backside', 'back'], ['Within', 'within']],
                                        'normal'],
             'swelling_question': ["Is there swelling of the knee?",
                                   [['Yes', 'swelling'], ['No', 'no_swelling'], ['Sometimes', 'some_swell']],
                                   'normal'],
             'swelling_location_question': ["Where is the swelling located?",
                                            ['In one spot', 'local'], ['Whole Knee', 'whole_knee'], 'normal'],
             'bending_question': ["Does bending the knee hurt?", ['Yes', 'bend_hurt'], ['No', 'bend_ok'],
                                  'normal'],
             'activities_question': ["Which of the following movements hurt?",
                                     [['Explosive Movements', 'explosive'], ['Repeated Movements', 'repeated'],
                                      ['Movement with torsions', 'torsion'], ['Sitting still', 'still'],
                                      ['Next', 'next']],
                                     'multi'],
             'extension_question': ["Which of the following movements hurts the most?",
                                    ['Extending the knee', 'extend'], ['Bending the knee', 'bend'], ['Both', 'both'],
                                    'normal']
              }


class WindowHandler:
    def __init__(self):
        self.stack = QStackedWidget()
        self.set_windows()
        self.stack.show()

    def set_windows(self):
        self.stack.addWidget(IntroductionWindow(self))
        for key, question in questions.items():
            # print(question[1], question[2], question[3])
            new_window = Window(self, question[0], question[1], question[2])
            self.stack.addWidget(new_window)

    def show_next_screen(self):
        print(self.stack.currentIndex())
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)
        self.stack.show()
