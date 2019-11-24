import pygame
from game_v2 import Game
from rankings import Rankings

pygame.init()
pygame.display.set_caption('Type Speed')


class Menu:

    def __init__(self):
        self.width = 1200
        self.height = 800
        self.white = 255, 255, 255
        self.red = 255, 0, 0
        self.green = 0, 255, 0
        self.yellow = 255, 255, 0
        self.black = 0, 0, 0
        self.start = 'Start Game'
        self.rankings = 'Ranking List'
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load('bg.png')
        self.font = pygame.font.SysFont(None, 50)
        self.start_text = self.font.render(self.start, True, self.black)
        self.rankings_text = self.font.render(self.rankings, True, self.black)
        self.start_button = self.draw_rect(self.start_text, 300)
        self.rankings_button = self.draw_rect(self.rankings_text, 400)

    def redraw_menu_window(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.start_text, self.draw_rect(self.start_text, 300))
        self.win.blit(self.rankings_text, self.draw_rect(self.rankings_text, 400))
        pygame.display.update()

    def draw_rect(self, text, height):
        text_rect = text.get_rect()
        text_rect.center = (self.width // 2, height)
        return text_rect

    def menu(self):
        run = True
        while run:
            self.redraw_menu_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()
                if self.start_button.collidepoint(pos):
                    self.start_text = self.mouse_motion_on_text(self.start, self.white)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        username, wpm = Game().run()
                        print(username, wpm)
                        Rankings().write_data(username, wpm)
                else:
                    self.start_text = self.mouse_motion_on_text(self.start, self.black)

                if self.rankings_button.collidepoint(pos):
                    self.rankings_text = self.mouse_motion_on_text(self.rankings, self.white)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.show_rankings()
                else:
                    self.rankings_text = self.mouse_motion_on_text(self.rankings, self.black)

            pygame.display.update()
        pygame.quit()

    @staticmethod
    def show_rankings():
        display = True
        while display:
            Rankings().display_rankings()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    display = False

    def mouse_motion_on_text(self, text, color):
        return self.font.render(text, True, color)
