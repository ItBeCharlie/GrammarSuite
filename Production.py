class Production:
    def __init__(self, string):
        self.string = string
        self.left = string.split(' -> ')[0]
        self.right = string.split(' -> ')[1]
        self.right_tokens = self.right.split()
        self.selection_set = []

    def __str__(self):
        return self.string
