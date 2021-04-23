import pygame

from mainMenu import MainMenuLevel
from musicManager import MusicManager
from inputManager import  InputManager
from controlsInstruction import ControlsLevel
from pauseManager import PauseManager
from level import *
from bestScores import BestScoresLevel
from scoreManager import ScoreManager
from lifeManager import LifeManager

class Game:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.isPlaying = True
        self.screen = pygame.display.set_mode([width, height])

        self.musicManager = MusicManager()
        self.inputManager = InputManager(self)
        self.pauseManager = PauseManager(self)
        self.scoreManager = ScoreManager()
        self.lifeManager = LifeManager()

        self.clock = pygame.time.Clock()

        self.showMainMenu()

    def isGamePlaying(self):
        return self.isPlaying

    def updateGame(self):
        self.inputManager.checkInput()
        self.currentLevel.updateLevel()

        self.clock.tick(60)
        pygame.display.flip()

    #Levels
    def showMainMenu(self):
        self.currentLevel = MainMenuLevel(self.screen, self)

    def showControlsInstruction(self):
        self.currentLevel = ControlsLevel(self.screen, self)

    def showBestScores(self):
        self.currentLevel = BestScoresLevel(self.screen, self)

    def showLevelOne(self):
        self.scoreManager.reset()
        self.lifeManager.reset()
        self.currentLevel = LevelOne(self.screen, self)

    def showEndingLevel(self):
        self.currentLevel = EndingLevel(self.screen, self)