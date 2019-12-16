import pygame
import math
import time

pygame.init()


class Frontend:

    __width: int
    __height: int

    def __init__(self):
        self.__width = 1200
        self.__height = 800

        self.__white = 255, 255, 255
        self.__red = 255, 0, 0
        self.__green = 0, 255, 0
        self.__yellow = 255, 255, 0
        self.__black = 0, 0, 0

        self.__wpm_level1 = range(1, 30)
        self.__wpm_level3 = 60
        self.__wpm_level2 = range(self.__wpm_level1[-1], self.__wpm_level3)

        self.__score = 0
        self.__wpm = 0
        self.__start_time = 0
        self.__timer = 0

        self.__data = []

        self.__text_to_write = '"And now here is my secret, a very simple secret: It is only with the heart that ' \
                               'one can see rightly; what is essential is invisible to the eye." ' \
                               '- Antoine de Saint-Exupery, The Little Prince'
        self.__words = self.__text_to_write.split(" ")
        self.__written_text = ''
        self.__correct_sentence = ''
        self.__start = 'Start Game'
        self.__rankings = 'Ranking List'

        self.__win = pygame.display.set_mode((self.__width, self.__height))
        self.__bg = pygame.image.load('bg.png')
        self.__font = pygame.font.SysFont(None, 35)
        self.__output_text = self.__font.render(self.__text_to_write, True, self.__white)
        self.__output_text_rect = self.__output_text.get_rect()
        self.__output_text_rect.center = (self.__width // 2, 400)
        self.__insert_text = self.__font.render('Insert Your Username', True, self.__white)
        self.__submit_text = self.__font.render('Press [SPACE] To Submit', True, self.__white)
        self.__input_text = self.__font.render(self.__written_text, True, self.__white)
        self.__timer_text = self.__font.render('Timer: ' + str(self.__timer), True, self.__white)
        self.__score_text = self.__font.render('Score: ' + str(self.__score), True, self.__white)
        self.__wpm_text = self.__font.render('wpm: ' + str(self.__wpm), True, self.wpm_coloring(self.__wpm))
        self.__text_length = self.__font.render('Text Length: ' + str(len(self.__text_to_write)) + ' chars', True,
                                                self.__white)
        self.__word_amount = self.__font.render('Words : ' + str(len(self.__words)) + ' words', True, self.__white)
        self.__username_label = self.__font.render('Username:', True, self.__white)
        self.__wpm_label = self.__font.render('wpm:', True, self.__white)
        self.__start_text = self.__font.render(self.__start, True, self.__black)
        self.__rankings_text = self.__font.render(self.__rankings, True, self.__black)

    def get_text_to_write(self):
        return self.__text_to_write

    def get_written_text(self):
        return self.__written_text

    def set_written_text(self, text):
        self.__written_text = text

    def get_words(self):
        return self.__words

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score

    def get_correct_sentence(self):
        return self.__correct_sentence

    def set_correct_sentence(self, sentence):
        self.__correct_sentence = sentence

    def get_wpm(self):
        return self.__wpm

    def set_start_time(self, start_time):
        self.__start_time = start_time

    def set_data(self, data):
        self.__data = data

    def get_start(self):
        return self.__start

    def get_rankings(self):
        return self.__rankings

    def get_start_text(self):
        return self.__start_text

    def get_rankings_text(self):
        return self.__rankings_text

    def set_start_text(self, text):
        self.__start_text = text

    def set_rankings_text(self, text):
        self.__rankings_text = text

    def redraw_game_window(self):
        self.time()
        self.wpm_count()
        self.info_text()

        self.__win.blit(self.__bg, (0, 0))
        self.blit_output_text(self.__text_to_write, (20, 400), self.__white)
        self.blit_output_text(self.__correct_sentence, (20, 400), self.__green)
        self.__win.blit(self.__input_text, (self.__width / 2 - self.__input_text.get_width() // 2, 600))
        self.__win.blit(self.__score_text, (self.__width - self.__width / 4 - self.__score_text.get_width() // 2, 50))
        self.__win.blit(self.__timer_text, (self.__width - self.__width / 4 - self.__timer_text.get_width() // 2, 80))
        self.__win.blit(self.__wpm_text, (self.__width / 2 - self.__wpm_text.get_width() // 2, 65))
        self.__win.blit(self.__text_length, (self.__width / 4 - self.__text_length.get_width() // 2, 50))
        self.__win.blit(self.__word_amount, (self.__width / 4 - self.__word_amount.get_width() // 2, 90))
        pygame.display.update()

    def draw_result_window(self):
        self.info_text()

        self.__win.blit(self.__bg, (0, 0))
        self.__win.blit(self.__input_text, (self.__width / 2 - self.__input_text.get_width() // 2, 600))
        self.__win.blit(self.__score_text, (self.__width - self.__width / 4 - self.__score_text.get_width() // 2, 50))
        self.__win.blit(self.__timer_text, (self.__width - self.__width / 4 - self.__timer_text.get_width() // 2, 80))
        self.__win.blit(self.__wpm_text, (self.__width / 2 - self.__wpm_text.get_width() // 2, 65))
        self.__win.blit(self.__text_length, (self.__width / 4 - self.__text_length.get_width() // 2, 50))
        self.__win.blit(self.__word_amount, (self.__width / 4 - self.__word_amount.get_width() // 2, 90))
        self.__win.blit(self.__insert_text, (self.__width / 2 - self.__insert_text.get_width() // 2, 550))
        self.__win.blit(self.__submit_text, (self.__width / 2 - self.__submit_text.get_width() // 2, 650))
        pygame.display.update()

    def info_text(self):
        self.__input_text = self.__font.render(self.__written_text, True, self.__white)
        self.__timer_text = self.__font.render('Timer: ' + str(self.__timer), True, self.__white)
        self.__score_text = self.__font.render('Score: ' + str(self.__score), True, self.__white)
        self.__wpm_text = self.__font.render('wpm: ' + str(self.__wpm), True, self.wpm_coloring(self.__wpm))
        self.__text_length = self.__font.render('Text Length: ' + str(len(self.__text_to_write)) + ' chars', True,
                                                self.__white)
        self.__word_amount = self.__font.render('Words : ' + str(len(self.__words)) + ' words', True, self.__white)

    def countdown(self):
        countdown_font = pygame.font.SysFont(None, 120)
        for i in range(3, 0, -1):
            self.__win.blit(self.__bg, (0, 0))
            countdown_text = countdown_font.render(str(i), True, self.__white)
            self.__win.blit(countdown_text, (self.__width / 2 - countdown_text.get_width() // 2,
                                             self.__height / 2 - countdown_text.get_height() // 2))
            time.sleep(1)
            pygame.display.update()
        time.sleep(1)

    def blit_output_text(self, text, pos, color):
        words = [word.split(' ') for word in text.splitlines()]
        space = self.__font.size(' ')[0]
        max_width, max_height = self.__win.get_size()
        word_height = 0
        x, y = pos
        for line in words:
            for word in line:
                word_surface = self.__font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
                self.__win.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height

    def time(self):
        self.__timer = math.trunc(time.time() - self.__start_time)

    def wpm_count(self):
        if self.__score != 0:
            self.__wpm = math.trunc((self.__score / self.__timer) * 60)

    def wpm_coloring(self, wpm):
        if wpm in self.__wpm_level1:
            return self.__green
        elif wpm in self.__wpm_level2:
            return self.__yellow
        elif wpm >= self.__wpm_level3:
            return self.__red
        else:
            return self.__white

    def display_rankings(self):
        self.__win.blit(self.__bg, (0, 0))

        y = 200

        self.__win.blit(self.__username_label, ((self.__width / 2 - self.__username_label.get_width() // 2) -
                                                self.__wpm_label.get_width(), y - 40))
        self.__win.blit(self.__wpm_label, ((self.__width / 2 - self.__wpm_label.get_width() // 2) +
                                           self.__username_label.get_width(), y - 40))

        end = self.size_of_data_to_show(10)

        for username, wpm in self.__data[:end]:
            username_text = self.__font.render(username, True, self.__white)
            wpm_text = self.__font.render(wpm, True, self.__white)

            self.__win.blit(username_text, ((self.__width / 2 - self.__username_label.get_width() // 2) -
                                            self.__wpm_label.get_width(), y))
            self.__win.blit(wpm_text, ((self.__width / 2 - self.__wpm_label.get_width() // 2) +
                                       self.__username_label.get_width(), y))
            y += 40

        submit_text = self.__font.render('Press [SPACE] To Continue', True, self.__white)
        self.__win.blit(submit_text, (self.__width / 2 - submit_text.get_width() // 2, y + 40))

        pygame.display.update()

    def size_of_data_to_show(self, end):
        if len(self.__data) < end:
            end = len(self.__data)
        return end

    def redraw_menu_window(self):
        self.__win.blit(self.__bg, (0, 0))
        self.__win.blit(self.__start_text, self.draw_rect(self.__start_text, 300))
        self.__win.blit(self.__rankings_text, self.draw_rect(self.__rankings_text, 400))
        pygame.display.update()

    def draw_rect(self, text, height):
        text_rect = text.get_rect()
        text_rect.center = (self.__width // 2, height)
        return text_rect
