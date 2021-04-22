
class PauseManager:

    def __init__(self, game):
        self.game = game
        self.IsPaused = False

    def reversePause(self):
        if self.game.currentLevel.isPausable():
            self.IsPaused = not self.IsPaused

    def isLevelPaused(self):
        return self.IsPaused

    def forceUnpause(self):
        self.IsPaused = False