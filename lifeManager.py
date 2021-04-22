
class LifeManager():

    def __init__(self):
        self.lifes = 3

    def subLife(self):
        self.lifes -= 1

    def reset(self):
        self.lifes = 3