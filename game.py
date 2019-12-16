import pygame
import time
from rules import Rules

pygame.init()
pygame.display.set_caption('Type Speed')


class Game:

    def __init__(self):
        self.__rules = Rules()
        self.__fe = self.__rules.get_frontend()
        self.__text_to_write = self.__fe.get_text_to_write()
        self.__clock = pygame.time.Clock()

    def run(self):
        self.__clock.tick(60)
        self.__fe.countdown()
        self.__fe.set_start_time(time.time())

        run = True
        while run:
            self.__fe.redraw_game_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if self.__rules.get_output_text_char_pos() == len(self.__text_to_write) and \
                        self.__fe.get_words()[self.__rules.get_word_position()] == self.__fe.get_written_text():
                    self.__fe.set_score(self.__fe.get_score() + 1)
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
                        key = self.__rules.rules_upper_case(key)
                    self.__rules.rules_game(key)
        return self.__fe, self.__rules
