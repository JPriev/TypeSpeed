import pygame
from rules import Rules


class Result:

    def __init__(self, fe, rules):
        self.__rules = rules
        self.__fe = fe

    def result(self):
        self.__fe.set_written_text('')
        self.__rules.set_char_position(0)
        run = True
        while run:
            self.__fe.draw_result_window()
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
                    run = self.__rules.rules_result(key, run)

        return self.__fe.get_written_text(), self.__fe.get_wpm()