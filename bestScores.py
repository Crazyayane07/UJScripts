import pygame

from baseLevel import BaseLevel

titleTextColor = (198, 212, 77)
buttonTextColour = (206, 73, 63)

FirstTextColour = (255,215,0)
SecondTextColour = (192,192,192)
ThirdTextColour = (205, 127, 50)

class BestScoresLevel(BaseLevel):

    def __init__(self, screen, game):
        super(BestScoresLevel, self).__init__(screen, game)
        self.scores = self.game.scoreManager.getSavedScores()
        self.scores.sort(reverse=True)

    def updateLevel(self):
        super(BestScoresLevel, self).updateLevel()

        font = pygame.font.Font(pygame.font.get_default_font(), 40)

        text_surface = font.render('Best Scores', True, titleTextColor)
        title_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 9))
        self.screen.blit(text_surface, title_text_rect)

        font = pygame.font.Font(pygame.font.get_default_font(), 30)

        if len(self.scores) > 0:
            text_surface = font.render(str(self.scores[0]), True, FirstTextColour)
            start_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2.5))
            self.screen.blit(text_surface, start_text_rect)

        if len(self.scores) > 1:
            text_surface = font.render(str(self.scores[1]), True, SecondTextColour)
            best_score_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2.05))
            self.screen.blit(text_surface, best_score_text_rect)

        if len(self.scores) > 2:
            text_surface = font.render(str(self.scores[2]), True, ThirdTextColour)
            quit_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 1.7))
            self.screen.blit(text_surface, quit_text_rect)

        text_surface = font.render('Back', True, buttonTextColour)
        back_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 1.1))
        self.screen.blit(text_surface, back_text_rect)

        self.checkMouseInput(back_text_rect)

    def checkMouseInput(self, back_text_rect):
        mousePosition = pygame.mouse.get_pos()

        if back_text_rect.collidepoint(mousePosition) and self.game.inputManager.isClicking():
            self.game.showMainMenu()