import pygame

class Ball(pygame.sprite.Sprite):

    def __init__(self, game, screen, player, obstacles, level):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.game = game
        self.player = player
        self.obstacles = obstacles
        self.level = level

        self.sprite = pygame.Surface((10, 10))
        self.sprite.fill((255, 255, 255))
        self.sprite = pygame.image.load("assets/GFX/pilka.png").convert()
        self.rect = self.sprite.get_rect()

        self.rect.x = 306
        self.rect.y = 390

        self.velocity = pygame.Vector2(-0.5, -2)

    def updateBall(self):
        if self.rect.y > self.game.height:
            self.LostBall()
        elif self.rect.y < 0:
            self.velocity = pygame.Vector2(self.velocity.x, abs(self.velocity.y))
        elif self.rect.x < 0:
            self.velocity = pygame.Vector2(self.velocity.x * -1, self.velocity.y)
        elif self.rect.x > self.game.width-10:
            self.velocity = pygame.Vector2(self.velocity.x * -1, self.velocity.y)
        elif self.rect.colliderect(self.player.rect):
            if(self.player.rect.x + 10 > self.rect.x + 5): # left side
                self.velocity = pygame.Vector2(self.velocity.x * 1.5, abs(self.velocity.y) * -1)
            elif(self.player.rect.x + 20 < self.rect.x + 5): # right side
                self.velocity = pygame.Vector2(self.velocity.x * -1.5, abs(self.velocity.y) * -1)
            else: #center
                self.velocity = pygame.Vector2(self.velocity.x, abs(self.velocity.y) * -1)

        for obstacle in self.obstacles:
            if self.rect.colliderect(obstacle.rect):
                self.game.scoreManager.addDefaultScore()
                if (obstacle.rect.x + 10 > self.rect.x + 5):  #left side
                    self.velocity = pygame.Vector2(self.velocity.x * 1.5, self.velocity.y)
                else:  #right  side
                    self.velocity = pygame.Vector2(self.velocity.x * -1.5, self.velocity.y)
                if (obstacle.rect.y + 5 < self.rect.y + 5):  #down side
                    self.velocity = pygame.Vector2(self.velocity.x, abs(self.velocity.y) * 1.5)
                else:  #up side
                    self.velocity = pygame.Vector2(self.velocity.x, abs(self.velocity.y) * -1.5)
                self.obstacles.remove(obstacle)

        self.limitVelocity()

        if(len(self.obstacles) <= 0):
            self.game.currentLevel = self.level.getNextLevel()

        self.rect.move_ip(self.velocity)
        self.screen.blit(self.sprite, self.rect)

    def LostBall(self):
        self.velocity = pygame.Vector2(-0.5, -2)
        self.rect.x = 306
        self.rect.y = 390
        self.player.OnLostBall()

    def limitVelocity(self):
        if self.velocity.x > 3:
            self.velocity.x = 3
        if self.velocity.x < -3:
            self.velocity.x = -3
        if self.velocity.y > 3:
            self.velocity.y = 3
        if self.velocity.y < -3:
            self.velocity.y = -3