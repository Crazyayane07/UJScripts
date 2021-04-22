import pygame

from game import Game

pygame.init()

pygame.display.set_caption("Arkanoid Pygame")

newGame = Game(640, 480)

while newGame.isGamePlaying():
    newGame.updateGame()

pygame.quit()