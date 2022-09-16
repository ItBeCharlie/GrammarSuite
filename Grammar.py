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
