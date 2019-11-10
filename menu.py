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
        self.startText = self.font.render(self.start, True, self.black)
        self.rankingsText = self.font.render(self.rankings, True, self.black)
        self.startButton = self.drawRect(self.startText, 300)
        self.rankingsButton = self.drawRect(self.rankingsText, 400)

    def redrawMenuWindow(self):
        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.startText, self.drawRect(self.startText, 300))
        self.win.blit(self.rankingsText, self.drawRect(self.rankingsText, 400))
        pygame.display.update()

    def drawRect(self, text, height):
        textRect = text.get_rect()
        textRect.center = (self.width // 2, height)
        return textRect

    def menu(self):
        run = True
        while run:
            self.redrawMenuWindow()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()
                if self.startButton.collidepoint(pos):
                    self.startText = self.mouseMotionOnText(self.start, self.white)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        username, wpm = Game().run()
                        print(username, wpm)
                        Rankings().writeData(username, wpm)
                else:
                    self.startText = self.mouseMotionOnText(self.start, self.black)

                if self.rankingsButton.collidepoint(pos):
                    self.rankingsText = self.mouseMotionOnText(self.rankings, self.white)
                    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        self.showRankings()
                else:
                    self.rankingsText = self.mouseMotionOnText(self.rankings, self.black)

            pygame.display.update()
        pygame.quit()

    def showRankings(self):
        display = True
        while display:
            Rankings().displayRankings()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    display = False

    def mouseMotionOnText(self, text, color):
        return self.font.render(text, True, color)
