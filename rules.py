from frontend import Frontend


class Rules:

    def __init__(self):
        self.__fe = Frontend()
        self.__char_position = 0
        self.__word_position = 0
        self.__output_text_char_pos = 0

    def get_char_position(self):
        return self.__char_position

    def get_word_position(self):
        return self.__word_position

    def get_output_text_char_pos(self):
        return self.__output_text_char_pos

    def get_frontend(self):
        return self.__fe

    def set_char_position(self, pos):
        self.__char_position = pos

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
                self.__fe.set_written_text(self.__fe.get_written_text() + key)
                self.__char_position += 1
                self.__output_text_char_pos += 1

    def rules_result(self, key, run):
        if key == 'backspace':
            if self.__char_position > 0:
                self.__char_position -= 1
                self.__fe.set_written_text(self.__fe.get_written_text()[:self.__char_position])
        elif key == 'space':
            if len(self.__fe.get_written_text()) != 0:
                run = False
        elif len(self.__fe.get_written_text()) < 13:
            self.__fe.set_written_text(self.__fe.get_written_text() + key)
            self.__char_position += 1
        return run

    def backspace_pressed(self):
        if self.__char_position > 0:
            self.__char_position -= 1
            self.__fe.set_written_text(self.__fe.get_written_text()[:self.__char_position])
            self.__output_text_char_pos -= 1

    def space_pressed(self):
        if self.__fe.get_written_text() == self.__fe.get_words()[self.__word_position]:
            self.__fe.set_written_text('')
            self.__word_position += 1
            self.__char_position = 0
            self.__fe.set_score(self.__fe.get_score() + 1)
            if self.__word_position != len(self.__fe.get_words()):
                self.__fe.set_correct_sentence(self.__fe.get_correct_sentence() +
                                               self.__fe.get_words()[self.__word_position - 1] + ' ')
            else:
                self.__fe.set_correct_sentence(self.__fe.get_correct_sentence() +
                                               self.__fe.get_words()[self.__word_position - 1])
        else:
            if self.__char_position != 0:
                self.__fe.set_written_text(self.__fe.get_written_text() + ' ')
                self.__char_position += 1
            else:
                self.__output_text_char_pos -= 1
        self.__output_text_char_pos += 1

    def in_bounds(self):
        return self.char_in_range() and self.word_in_range()

    def char_in_range(self):
        return self.__char_position in range(0, len(self.__fe.get_words()[self.__word_position]))

    def word_in_range(self):
        return self.__word_position in range(0, len(self.__fe.get_words()))
