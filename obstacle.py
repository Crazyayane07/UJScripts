import pygame

class Obstacle(pygame.sprite.Sprite):

    def __init__(self, screen, game, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.screen = screen

        self.sprite = pygame.Surface((31, 18))
        self.sprite.fill((255, 0, 0))
        self.sprite = pygame.image.load("assets/GFX/obstacle.png").convert()
        self.rect = self.sprite.get_rect()

        self.rect.x = x
        self.rect.y = y

    def updateObstacle(self):
        self.screen.blit(self.sprite, self.rect)