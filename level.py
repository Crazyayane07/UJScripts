import pygame

from baseLevel import BaseLevel
from ending import EndingLevel
from player import Player
from obstacle import Obstacle
from ball import Ball

buttonTextColour = (206, 73, 63)
healthTextColor = (115, 239, 0)
scoreTextColor = (249, 239, 0)

class Level(BaseLevel):

    def __init__(self, screen, game):
        super(Level, self).__init__(screen, game)
        self.player = None
        self.ball = None
        self.obstacles = []

    def isPausable(self):
        return True

    def updateLevel(self):
        super(Level, self).updateLevel()
        if not self.isPaused():
            self.player.updatePlayer()
            self.ball.updateBall()

            for obstacle in self.obstacles:
                obstacle.updateObstacle()

            font = pygame.font.Font(pygame.font.get_default_font(), 30)

            text_surface = font.render(self.levelText, True, buttonTextColour)
            start_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 8))
            self.screen.blit(text_surface, start_text_rect)

            text_surface = font.render(str(self.game.lifeManager.lifes), True, healthTextColor)
            start_text_rect = text_surface.get_rect(center=(self.width / 1.1, self.height / 8))
            self.screen.blit(text_surface, start_text_rect)

            text_surface = font.render(str(self.game.scoreManager.score), True, scoreTextColor)
            start_text_rect = text_surface.get_rect(center=(self.width / 9.0, self.height / 8))
            self.screen.blit(text_surface, start_text_rect)

        self.checkInput()

    def checkInput(self):
        if self.game.inputManager.isPressingNextLevelButton:
            self.game.pauseManager.forceUnpause()
            self.game.currentLevel = self.getNextLevel()
            self.game.inputManager.resetIsPressingNextLevelButton()

    def getNextLevel(self):
        return LevelOne(self.screen, self.game)

    def checkIfFinishedLevel(self):
        for obstacle in self.obstacles:
            if obstacle is not None:
                return False
            return True

class LevelOne(Level):

    def __init__(self, screen, game):
        super(Level, self).__init__(screen, game)
        self.levelText = "Level 1"
        self.player = Player(self.screen, self.game)

        self.obstacles = []
        self.obstacles.append(Obstacle(screen, game, 306, 250))

        self.ball = Ball(self.game, self.screen, self.player, self.obstacles, self)

    def getNextLevel(self):
        return LevelTwo(self.screen, self.game)

class LevelTwo(Level):

    def __init__(self, screen, game):
        super(Level, self).__init__(screen, game)
        self.levelText = "Level 2"
        self.player = Player(self.screen, self.game)

        self.obstacles = []
        self.obstacles.append(Obstacle(screen, game, 306, 250))
        self.obstacles.append(Obstacle(screen, game, 306, 200))

        self.ball = Ball(self.game, self.screen, self.player, self.obstacles, self)

    def getNextLevel(self):
        return LevelThree(self.screen, self.game)

class LevelThree(Level):

    def __init__(self, screen, game):
        super(Level, self).__init__(screen, game)
        self.levelText = "Level 3"
        self.player = Player(self.screen, self.game)

        self.obstacles = []
        self.obstacles.append(Obstacle(screen, game, 306, 250))
        self.obstacles.append(Obstacle(screen, game, 506, 250))
        self.obstacles.append(Obstacle(screen, game, 106, 250))

        self.ball = Ball(self.game, self.screen, self.player, self.obstacles, self)

    def getNextLevel(self):
        return LevelFour(self.screen, self.game)

class LevelFour(Level):

    def __init__(self, screen, game):
        super(Level, self).__init__(screen, game)
        self.levelText = "Level 4"
        self.player = Player(self.screen, self.game)

        self.obstacles = []
        self.obstacles.append(Obstacle(screen, game, 306, 250))
        self.obstacles.append(Obstacle(screen, game, 506, 250))
        self.obstacles.append(Obstacle(screen, game, 106, 250))
        self.obstacles.append(Obstacle(screen, game, 306, 200))

        self.ball = Ball(self.game, self.screen, self.player, self.obstacles, self)

    def getNextLevel(self):
        return LevelFive(self.screen, self.game)

class LevelFive(Level):

    def __init__(self, screen, game):
        super(Level, self).__init__(screen, game)
        self.levelText = "Level 5"
        self.player = Player(self.screen, self.game)

        self.obstacles = []
        self.obstacles.append(Obstacle(screen, game, 306, 250))
        self.obstacles.append(Obstacle(screen, game, 506, 250))
        self.obstacles.append(Obstacle(screen, game, 106, 250))
        self.obstacles.append(Obstacle(screen, game, 306, 200))
        self.obstacles.append(Obstacle(screen, game, 306, 300))

        self.ball = Ball(self.game, self.screen, self.player, self.obstacles, self)

    def getNextLevel(self):
        return EndingLevel(self.screen, self.game)