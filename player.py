import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    def __init__(self, screen, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = screen

        self.sprite = pygame.Surface((29, 7))
        self.sprite.fill((255, 0, 0))
        self.sprite = pygame.image.load("assets/GFX/player.png").convert()
        self.rect = self.sprite.get_rect()

        self.rect.x = 306
        self.rect.y = 400

    def updatePlayer(self):
        self.checkInput()
        self.screen.blit(self.sprite, self.rect)

    def checkInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.x - 3 > -3:
                self.rect.x -= 3
        if keys[pygame.K_RIGHT]:
            if self.rect.x - 3 < 612:
                self.rect.x += 3

    def OnLostBall(self):
        self.game.lifeManager.subLife()
        if self.game.lifeManager.lifes <= 0:
            self.game.showEndingLevel()