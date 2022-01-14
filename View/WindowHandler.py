from PySide2.QtWidgets import QStackedWidget
from View.Window import *
from View.IntroductionWindow import *
from View.FinalWindow import *

questions = [["What is your age?",
                              [['0-12', '1'], ['12-18', '2'], ['18-39', '3'], ['39-55', '4'], ['55+', '5']],
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
             ["Which of the following movements hurt?\nSelect a movement and indicate the degree"
                                     " to which it hurts with the sliders.\n(Left = mild pain, Right = extreme pain)",
                                     [['Explosive Movements', 'explosive'], ['Repeated Movements', 'repeated'],
                                      ['Movement with torsions', 'torsion'], ['Sitting still', 'still']],
                                     'multi']
             ]

treatment = {'Jumpers knee': "Reduce the load on your knee relative to your usual strength.\nAvoid jumping and peak "
                             "exercises until the pain subsides. If the pain returns, lower your overall physical load."
                             "\nTrain your upper leg and hip stabilizers with alternating leg movements (avoid double"
                             " leg exercises such as squats).\nEstimated time until recovery: 6 months."
             }


class WindowHandler:
    def __init__(self, knowledge_base):
        self.stack = QStackedWidget()
        self.kb = knowledge_base
        self.diagnosis = "Jumpers knee"
        self.start = True
        self.idx = 0
        self.treatment = {
            'Jumpers knee': "Reduce the load on your knee relative to your usual strength.\nAvoid jumping and peak "
                            "exercises until the pain subsides. If the pain returns, lower your overall physical load."
                            "\nTrain your upper leg and hip stabilizers with alternating leg movements (avoid double"
                            " leg exercises such as squats).\nEstimated time until recovery: 6 months."
            }
        self.set_window()
        self.stack.show()

    def set_window(self):
        if self.start:
            self.stack.addWidget(IntroductionWindow(self))
            self.start = False
        elif self.idx > len(questions):
            self.stack.addWidget(FinalWindow(self))
        else:
            # print(question[1], question[2], question[3])
            print("question[0] should be the key variable", questions[self.idx][0])
            new_window = Window(self, questions[self.idx][0], questions[self.idx][1], questions[self.idx][2])
            self.stack.addWidget(new_window)
            self.idx += 1

    def show_next_screen(self):
        self.set_window()
        print(self.stack.currentIndex())
        self.stack.setCurrentIndex(self.stack.currentIndex() + 1)
        self.stack.widget(self.stack.currentIndex()).diagnosis = self.diagnosis
        self.stack.show()
