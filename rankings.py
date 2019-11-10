import pygame


class Rankings:

    def __init__(self):
        self.width = 1200
        self.height = 800
        self.white = 255, 255, 255
        self.black = 0, 0, 0
        self.path = 'Data.csv'
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load('bg.png')
        self.font = pygame.font.SysFont(None, 50)
        self.data = [line.strip().split(',') for line in open(self.path)]

    def sortData(self):
        self.data.sort(reverse=True, key=lambda x: x[1])

    def readData(self):
        return self.data

    def displayRankings(self):
        self.sortData()
        self.win.blit(self.bg, (0, 0))
        y = 200
        usernameLabel = self.font.render('Username:', True, self.white)
        wpmLabel = self.font.render('wpm:', True, self.white)
        self.win.blit(usernameLabel, ((self.width / 2 - usernameLabel.get_width() // 2) - wpmLabel.get_width(), y - 40))
        self.win.blit(wpmLabel, ((self.width / 2 - wpmLabel.get_width() // 2) + usernameLabel.get_width(), y - 40))

        end = 10
        if len(self.data) < 10:
            end = len(self.data)

        for i in range(0, end):
            username = self.data[i][0]
            wpm = self.data[i][1]
            usernameText = self.font.render(username, True, self.white)
            wpmText = self.font.render(wpm, True, self.white)
            self.win.blit(usernameText, ((self.width / 2 - usernameLabel.get_width() // 2) - wpmLabel.get_width(), y))
            self.win.blit(wpmText, ((self.width / 2 - wpmLabel.get_width() // 2) + usernameLabel.get_width(), y))
            y += 40

        submitText = self.font.render('Press [SPACE] To Continue', True, self.white)
        self.win.blit(submitText, (self.width / 2 - submitText.get_width() // 2, y + 40))

        pygame.display.update()

    def writeToRankings(self):
        pass

    def writeData(self, username, wpm):
        file = open(self.path, "a")
        file.write('\n' + username + ',' + str(wpm))
        file.close()
