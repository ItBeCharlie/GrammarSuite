class Grammar:
    def __init__(self, productions):
        self.productions = productions
        # Left side of first production is default starting state
        self.start_production = productions[0].left

    def __str__(self):
        s = f'Start State: {self.start_production}'
        for production in self.productions:
            s += f'\n{production}'
        return s

    def length(self, production):
        return len(self.productions[production].right)

    def index(self, production_string):
        for index, production in enumerate(self.productions):
            if str(production) == production_string:
                return index
        return None
