import pygame

from baseLevel import BaseLevel

titleTextColor = (198, 212, 77)
buttonTextColour = (206, 73, 63)

class MainMenuLevel(BaseLevel):

    def __init__(self, screen, game):
        super(MainMenuLevel, self).__init__(screen, game)

    def updateLevel(self):
        super(MainMenuLevel, self).updateLevel()

        font = pygame.font.Font(pygame.font.get_default_font(), 60)

        text_surface = font.render('Arkanoid', True, titleTextColor)
        title_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 9))
        self.screen.blit(text_surface, title_text_rect)

        font = pygame.font.Font(pygame.font.get_default_font(), 30)

        text_surface = font.render('Start Game', True, buttonTextColour)
        start_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2.5))
        self.screen.blit(text_surface, start_text_rect)

        text_surface = font.render('Best Scores', True, buttonTextColour)
        best_score_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2.05))
        self.screen.blit(text_surface, best_score_text_rect)

        text_surface = font.render('Quit Game', True, buttonTextColour)
        quit_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 1.7))
        self.screen.blit(text_surface, quit_text_rect)

        text_surface = font.render('Controls', True, buttonTextColour)
        controls_text_rect = text_surface.get_rect(center=(self.width / 2, self.height/ 1.2))
        self.screen.blit(text_surface, controls_text_rect)

        self.checkMouseInput(start_text_rect, best_score_text_rect, quit_text_rect, controls_text_rect)


    def checkMouseInput(self, start_text_rect, best_score_text_rect, quit_text_rect, controls_text_rect):
        mousePosition = pygame.mouse.get_pos()

        if start_text_rect.collidepoint(mousePosition) and self.game.inputManager.isClicking():
            self.game.showLevelOne()
        elif best_score_text_rect.collidepoint(mousePosition) and self.game.inputManager.isClicking():
            self.game.showBestScores()
        elif quit_text_rect.collidepoint(mousePosition) and self.game.inputManager.isClicking():
            self.game.isPlaying = False
        elif controls_text_rect.collidepoint(mousePosition) and self.game.inputManager.isClicking():
            self.game.showControlsInstruction()