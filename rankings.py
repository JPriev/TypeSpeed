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

    def sort_data(self):
        self.data.sort(reverse=True, key=lambda x: x[1])

    def read_data(self):
        return self.data

    def display_rankings(self):
        self.sort_data()
        self.win.blit(self.bg, (0, 0))
        y = 200
        username_label = self.font.render('Username:', True, self.white)
        wpm_label = self.font.render('wpm:', True, self.white)
        self.win.blit(username_label, ((self.width / 2 - username_label.get_width() // 2) -
                                       wpm_label.get_width(), y - 40))
        self.win.blit(wpm_label, ((self.width / 2 - wpm_label.get_width() // 2) + username_label.get_width(), y - 40))

        end = 10
        if len(self.data) < 10:
            end = len(self.data)

        for i in range(0, end):
            username = self.data[i][0]
            wpm = self.data[i][1]
            username_text = self.font.render(username, True, self.white)
            wpm_text = self.font.render(wpm, True, self.white)
            self.win.blit(username_text, ((self.width / 2 - username_label.get_width() // 2) -
                                          wpm_label.get_width(), y))
            self.win.blit(wpm_text, ((self.width / 2 - wpm_label.get_width() // 2) + username_label.get_width(), y))
            y += 40

        submit_text = self.font.render('Press [SPACE] To Continue', True, self.white)
        self.win.blit(submit_text, (self.width / 2 - submit_text.get_width() // 2, y + 40))

        pygame.display.update()

    def write_data(self, username, wpm):
        file = open(self.path, "a")
        file.write('\n' + username + ',' + str(wpm))
        file.close()
