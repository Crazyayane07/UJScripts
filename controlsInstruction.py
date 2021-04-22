import pygame

from baseLevel import BaseLevel

titleTextColor = (198, 212, 77)
defaultTextColor = (187, 114, 151)
buttonTextColour = (206, 73, 63)

class ControlsLevel(BaseLevel):

        def __init__(self, screen, game):
            super(ControlsLevel, self).__init__(screen, game)

        def updateLevel(self):
            super(ControlsLevel, self).updateLevel()

            font = pygame.font.Font(pygame.font.get_default_font(), 40)

            text_surface = font.render('Controls', True, titleTextColor)
            title_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 9))
            self.screen.blit(text_surface, title_text_rect)

            font = pygame.font.Font(pygame.font.get_default_font(), 20)

            text_surface = font.render('Arrows -> moving', True, defaultTextColor)
            text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2.5))
            self.screen.blit(text_surface, text_rect)

            text_surface = font.render('Mouse -> UI interaction', True, defaultTextColor)
            text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 2.2))
            self.screen.blit(text_surface, text_rect)

            text_surface = font.render('SPACEBAR -> pause', True, defaultTextColor)
            text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 1.95))
            self.screen.blit(text_surface, text_rect)

            text_surface = font.render('ENTER -> force next stage', True, defaultTextColor)
            text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 1.75))
            self.screen.blit(text_surface, text_rect)

            font = pygame.font.Font(pygame.font.get_default_font(), 30)

            text_surface = font.render('Back', True, buttonTextColour)
            back_text_rect = text_surface.get_rect(center=(self.width / 2, self.height / 1.1))
            self.screen.blit(text_surface, back_text_rect)

            self.checkMouseInput(back_text_rect)

        def checkMouseInput(self, back_text_rect):
            mousePosition = pygame.mouse.get_pos()

            if back_text_rect.collidepoint(mousePosition) and self.game.inputManager.isClicking():
                self.game.showMainMenu()