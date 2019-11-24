import pygame
import math
import time

pygame.init()
pygame.display.set_caption('Type Speed')


class Game:

    width: int
    height: int

    def __init__(self):
        self.username = ''
        self.width = 1200
        self.height = 800
        self.white = 255, 255, 255
        self.red = 255, 0, 0
        self.green = 0, 255, 0
        self.yellow = 255, 255, 0
        self.black = 0, 0, 0
        self.score = 0
        self.char_position = 0
        self.word_position = 0
        self.output_text_char_pos = 0
        self.start_time = 0
        self.timer = 0
        self.wpm = 0
        self.text_to_write = '"And now here is my secret, a very simple secret: It is only with the heart that ' \
                             'one can see rightly; what is essential is invisible to the eye." ' \
                             '- Antoine de Saint-Exupery, The Little Prince'
        self.words = self.text_to_write.split(" ")
        self.written_text = ''
        self.correct_sentence = ''
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load('bg.png')
        self.font = pygame.font.SysFont(None, 35)
        self.output_text = self.font.render(self.text_to_write, True, self.white)
        self.output_text_rect = self.output_text.get_rect()
        self.output_text_rect.center = (self.width // 2, 400)
        self.insert_text = self.font.render('Insert Your Username', True, self.white)
        self.submit_text = self.font.render('Press [SPACE] To Submit', True, self.white)
        self.input_text = self.font.render(self.written_text, True, self.white)
        self.timer_text = self.font.render('Timer: ' + str(self.timer), True, self.white)
        self.score_text = self.font.render('Score: ' + str(self.score), True, self.white)
        self.wpm_text = self.font.render('wpm: ' + str(self.wpm), True, self.wpm_coloring())
        self.text_length = self.font.render('Text Length: ' + str(len(self.text_to_write)) + ' chars', True, self.white)
        self.word_amount = self.font.render('Words : ' + str(len(self.words)) + ' words', True, self.white)
        self.clock = pygame.time.Clock()

    def run(self):
        self.clock.tick(60)
        self.countdown()
        self.start_time = time.time()
        run = True
        while run:
            self.redraw_game_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if self.output_text_char_pos == len(self.text_to_write) and \
                        self.words[self.word_position] == self.written_text:
                    self.score += 1
                    run = False

                if event.type == pygame.KEYDOWN and (event.key in range(pygame.K_a, pygame.K_DELETE) or
                                                     event.key in list([pygame.K_COMMA, pygame.K_PERIOD,
                                                                        pygame.K_QUESTION, pygame.K_SEMICOLON,
                                                                        pygame.K_EXCLAIM, pygame.K_QUOTEDBL,
                                                                        pygame.K_QUOTE, pygame.K_BACKSPACE,
                                                                        pygame.K_SPACE, pygame.K_CAPSLOCK,
                                                                        pygame.KMOD_SHIFT, pygame.K_MINUS])):
                    key = pygame.key.name(event.key)
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        key = self.rules_upper_case(key)

                    self.rules_game(key)

                print(event)

            pygame.display.update()
        self.char_position = 0
        return self.result()

    def redraw_game_window(self):
        self.time()
        self.wpm_count()
        self.info_text()

        self.win.blit(self.bg, (0, 0))
        self.blit_output_text(self.text_to_write, (20, 400), self.white)
        self.blit_output_text(self.correct_sentence, (20, 400), self.green)
        self.win.blit(self.input_text, (self.width / 2 - self.input_text.get_width() // 2, 600))
        self.win.blit(self.score_text, (self.width - self.width / 4 - self.score_text.get_width() // 2, 50))
        self.win.blit(self.timer_text, (self.width - self.width / 4 - self.timer_text.get_width() // 2, 80))
        self.win.blit(self.wpm_text, (self.width / 2 - self.wpm_text.get_width() // 2, 65))
        self.win.blit(self.text_length, (self.width / 4 - self.text_length.get_width() // 2, 50))
        self.win.blit(self.word_amount, (self.width / 4 - self.word_amount.get_width() // 2, 90))
        pygame.display.update()

    def draw_result_window(self):
        self.info_text()

        self.win.blit(self.bg, (0, 0))
        self.win.blit(self.input_text, (self.width / 2 - self.input_text.get_width() // 2, 600))
        self.win.blit(self.score_text, (self.width - self.width / 4 - self.score_text.get_width() // 2, 50))
        self.win.blit(self.timer_text, (self.width - self.width / 4 - self.timer_text.get_width() // 2, 80))
        self.win.blit(self.wpm_text, (self.width / 2 - self.wpm_text.get_width() // 2, 65))
        self.win.blit(self.text_length, (self.width / 4 - self.text_length.get_width() // 2, 50))
        self.win.blit(self.word_amount, (self.width / 4 - self.word_amount.get_width() // 2, 90))
        self.win.blit(self.insert_text, (self.width / 2 - self.insert_text.get_width() // 2, 550))
        self.win.blit(self.submit_text, (self.width / 2 - self.submit_text.get_width() // 2, 650))
        pygame.display.update()

    def info_text(self):
        pass
        self.input_text = self.font.render(self.written_text, True, self.white)
        self.timer_text = self.font.render('Timer: ' + str(self.timer), True, self.white)
        self.score_text = self.font.render('Score: ' + str(self.score), True, self.white)
        self.wpm_text = self.font.render('wpm: ' + str(self.wpm), True, self.wpm_coloring())
        self.text_length = self.font.render('Text Length: ' + str(len(self.text_to_write)) + ' chars', True, self.white)
        self.word_amount = self.font.render('Words : ' + str(len(self.words)) + ' words', True, self.white)

    @staticmethod
    def rules_upper_case(key):
        key = key.upper()
        if key == "'":
            key = '"'
        elif key == ';':
            key = ':'
        return key

    def rules_game(self, key):
        if key == 'backspace':
            self.backspace_pressed()

        elif key == 'space':
            self.space_pressed()

        else:
            if self.in_bounds():
                self.written_text += key
                self.char_position += 1
                self.output_text_char_pos += 1

    def rules_result(self, key, run):
        if key == 'backspace':
            if self.char_position > 0:
                self.char_position -= 1
                self.written_text = self.written_text[:self.char_position]
        elif key == 'space':
            if len(self.written_text) != 0:
                run = False
        elif len(self.written_text) < 13:
            self.written_text += key
            self.char_position += 1
        return run

    def backspace_pressed(self):
        if self.char_position > 0:
            self.char_position -= 1
            self.written_text = self.written_text[:self.char_position]
            self.output_text_char_pos -= 1

    def space_pressed(self):
        if self.written_text == self.words[self.word_position]:
            self.written_text = ''
            self.word_position += 1
            self.char_position = 0
            self.score += 1
            if self.word_position != len(self.words):
                self.correct_sentence += self.words[self.word_position - 1] + ' '
            else:
                self.correct_sentence += self.words[self.word_position - 1]
        else:
            if self.char_position != 0:
                self.written_text += ' '
                self.char_position += 1
            else:
                self.output_text_char_pos -= 1
        self.output_text_char_pos += 1

    def in_bounds(self):
        return self.char_position in range(0, len(self.words[self.word_position])) \
               and self.word_position in range(0, len(self.words))

    def time(self):
        self.timer = math.trunc(time.time() - self.start_time)

    def wpm_count(self):
        if self.score != 0:
            self.wpm = math.trunc((self.score / self.timer) * 60)

    def wpm_coloring(self):
        if self.wpm in range(1, 30):
            return self.green
        elif self.wpm in range(31, 61):
            return self.yellow
        elif self.wpm > 60:
            return self.red
        else:
            return self.white

    def countdown(self):
        countdown_font = pygame.font.SysFont(None, 120)
        for i in range(3, 0, -1):
            self.win.blit(self.bg, (0, 0))
            countdown_text = countdown_font.render(str(i), True, self.white)
            self.win.blit(countdown_text, (self.width / 2 - countdown_text.get_width() // 2,
                                           self.height / 2 - countdown_text.get_height() // 2))
            time.sleep(1)
            pygame.display.update()
        time.sleep(1)

    def result(self):
        self.written_text = ''
        run = True
        while run:
            self.draw_result_window()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.KEYDOWN and (event.key in range(pygame.K_a, pygame.K_DELETE) or
                                                     event.key in range(pygame.K_0, pygame.K_COLON) or
                                                     event.key in list([pygame.K_BACKSPACE, pygame.K_SPACE,
                                                                        pygame.KMOD_SHIFT])):
                    key = pygame.key.name(event.key)
                    if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                        key = pygame.key.name(event.key).upper()

                    run = self.rules_result(key, run)

            pygame.display.update()
        return self.written_text, self.wpm

    def blit_output_text(self, text, pos, color):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = self.font.size(' ')[0]  # The width of a space.
        max_width, max_height = self.win.get_size()
        word_height = 0
        x, y = pos
        for line in words:
            for word in line:
                word_surface = self.font.render(word, True, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                self.win.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.
