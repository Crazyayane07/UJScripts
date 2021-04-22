import pygame
from pygame.locals import *

class InputManager:

    def __init__(self, game):
        self.game = game
        self.clicking = False
        self.isPressingPauseButton = False
        self.isPressingNextLevelButton = False

    def checkInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.isPlaying = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.clicking = True
            if event.type == MOUSEBUTTONUP:
                if event.button == 1:
                    self.clicking = False
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.isPressingPauseButton:
                        self.game.pauseManager.reversePause()
                        self.isPressingPauseButton = True
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    if not self.isPressingNextLevelButton:
                        self.isPressingNextLevelButton = True
            if event.type == KEYUP:
                self.isPressingPauseButton = False
                self.isPressingNextLevelButton = False

    def isClicking(self):
        return self.clicking

    def resetIsPressingNextLevelButton(self):
        self.isPressingNextLevelButton = False