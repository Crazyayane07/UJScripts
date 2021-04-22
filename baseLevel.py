
class BaseLevel():
    def __init__(self, screen, game):
        self.screen = screen
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        self.game = game

        self.musicAsset = "assets/music/sounds_intro.mp3"
        self.game.musicManager.playMusic(self.musicAsset, 0.2)

    def updateLevel(self):
        if not self.isPaused():
            self.screen.fill((0, 0, 0))

    def isPausable(self):
        return False

    def isPaused(self):
        if self.isPausable():
            return self.game.pauseManager.isLevelPaused()
        return False