import pygame
from game import Game
from result import Result
from rankings import Rankings


class Command:

    def execute(self):
        pass


class StartButton:

    @staticmethod
    def start_button_pressed(event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            fe, rules = Game().run()
            username, wpm = Result(fe, rules).result()
            Rankings().write_data(username, wpm)


class RankingsButton:

    @staticmethod
    def rankings_button_pressed(event_type):
        if event_type == pygame.MOUSEBUTTONDOWN:
            Rankings().show_rankings()


class StartButtonCommand(Command):

    def __init__(self, start_button: StartButton, pet):
        self.__start_button = start_button
        self.__type = pet

    def execute(self):
        self.__start_button.start_button_pressed(self.__type)


class RankingsButtonCommand(Command):

    def __init__(self, rankings_button: RankingsButton, pet):
        self.__rankings_button = rankings_button
        self.__type = pet

    def execute(self):
        self.__rankings_button.rankings_button_pressed(self.__type)


class ButtonInvoker:

    def __init__(self, command: Command):
        self.__command = command

    def set_command(self, command: Command):
        self.__command = command

    def get_command(self):
        print(self.__command.__class__.__name__)

    def invoke(self):
        self.__command.execute()
