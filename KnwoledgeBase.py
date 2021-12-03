
class KnowledgeBase:

    def __init__(self):

        self.KB = {}

        self.KB["rules"] = [(["croak", "sings"], "frog"),    #([premise1, premise2], conclusion)  -> all conjunctions
                       (["sings", "yellow"], "bird"),
                       (["talks", "walks"], "human"),
                       (["frog"], "swims"),
                       (["bird"], "flies")
                       ]

        self.KB["symptoms"] = [("croak", "tim"), ("sings", "tim"),
                       ("talks", "maria"),
                       ("yellow", "tom"), ("sings", "tom"),
                       ("bird", "nick")]

        self.KB["diagnoses"] = ["tim", "tom", "maria", "nick"]


