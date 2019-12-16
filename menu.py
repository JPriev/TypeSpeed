import pygame
from frontend import Frontend
import button_commands

pygame.init()
pygame.display.set_caption('Type Speed')


class Menu:

    def __init__(self):
        self.__width = 1200
        self.__height = 800

        self.__white = 255, 255, 255
        self.__red = 255, 0, 0
        self.__green = 0, 255, 0
        self.__yellow = 255, 255, 0
        self.__black = 0, 0, 0

        self.__fe = Frontend()
        self.__font = pygame.font.SysFont(None, 50)
        self.__start_button = self.__fe.draw_rect(self.__fe.get_start_text(), 300)
        self.__rankings_button = self.__fe.draw_rect(self.__fe.get_rankings_text(), 400)

        self.__start = button_commands.StartButton()
        self.__rankings = button_commands.RankingsButton()

    def menu(self):
        run = True
        while run:
            self.__fe.redraw_menu_window()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                pos = pygame.mouse.get_pos()
                if self.__start_button.collidepoint(pos):
                    self.__fe.set_start_text(self.mouse_motion_on_text(self.__fe.get_start(), self.__white))
                    command_start = button_commands.StartButtonCommand(self.__start, event.type)
                    button_invoker = button_commands.ButtonInvoker(command_start)
                    button_invoker.invoke()
                else:
                    self.__fe.set_start_text(self.mouse_motion_on_text(self.__fe.get_start(), self.__black))

                if self.__rankings_button.collidepoint(pos):
                    self.__fe.set_rankings_text(self.mouse_motion_on_text(self.__fe.get_rankings(), self.__white))
                    command_rankings = button_commands.RankingsButtonCommand(self.__rankings, event.type)
                    button_invoker = button_commands.ButtonInvoker(command_rankings)
                    button_invoker.invoke()
                else:
                    self.__fe.set_rankings_text(self.mouse_motion_on_text(self.__fe.get_rankings(), self.__black))

            pygame.display.update()
        pygame.quit()

    def mouse_motion_on_text(self, text, color):
        return self.__font.render(text, True, color)
