import pygame

from baseLevel import BaseLevel

ScoreTextColour = (240,230,140)
TextColour = (178,34,34)

class EndingLevel(BaseLevel):

    def __init__(self, screen, game):
        super(EndingLevel, self).__init__(screen, game)
        self.game.scoreManager.saveNewScore()

    def updateLevel(self):
        super(EndingLevel, self).updateLevel()

        font = pygame.font.Font(pygame.font.get_default_font(), 60)

        text_surface = font.render('The End', True, TextColour)
        title_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 9))
        self.screen.blit(text_surface, title_text_rect)

        font = pygame.font.Font(pygame.font.get_default_font(), 30)

        scoreText = "Final score: " + str(self.game.scoreManager.score)
        text_surface = font.render(scoreText, True, ScoreTextColour)
        start_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2.5))
        self.screen.blit(text_surface, start_text_rect)