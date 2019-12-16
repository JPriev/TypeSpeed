import pygame
from frontend import Frontend


class Rankings:

    def __init__(self):
        self.__fe = Frontend()
        self.__path = 'Data.csv'
        self.__data = [line.strip().split(',') for line in open(self.__path)]

    def sort_data(self):
        self.__data.sort(reverse=True, key=lambda x: x[1])

    def write_data(self, username, wpm):
        file = open(self.__path, "a")
        file.write('\n' + username + ',' + str(wpm))
        file.close()

    def show_rankings(self):
        self.sort_data()
        self.__fe.set_data(self.__data)
        display = True
        while display:
            self.__fe.display_rankings()
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    display = False
