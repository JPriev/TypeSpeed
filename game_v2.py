import pygame
import math
import time

pygame.init()

pygame.display.set_caption('Type Speed')


class Game:

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
        self.charPosition = 0
        self.wordPosition = 0
        self.outputTextCharPos = 0
        self.startTime = 0
        self.timer = 0
        self.wpm = 0
        #self.textToWrite = 'aaaa ssss'
        self.textToWrite = '"And now here is my secret, a very simple secret: It is only with the heart that ' \
                           'one can see rightly; what is essential is invisible to the eye." ' \
                           '- Antoine de Saint-Exupery, The Little Prince'
        self.words = self.textToWrite.split(" ")
        self.writtenText = ''
        self.correctSentence = ''
        self.capsLkFlag = False  # patikrint su subprocess ar capslock active
        self.win = pygame.display.set_mode((self.width, self.height))
        self.bg = pygame.image.load('bg.png')
        self.font = pygame.font.SysFont(None, 35)
        self.outputText = self.font.render(self.textToWrite, True, self.white)
        self.outputTextRect = self.outputText.get_rect()
        self.outputTextRect.center = (self.width // 2, 400)
        self.clock = pygame.time.Clock()

    def redrawGameWindow(self):
        self.time()
        self.wordsPerMinute()

        inputText = self.font.render(self.writtenText, True, self.white)
        timerText = self.font.render('Timer: ' + str(self.timer), True, self.white)
        scoreText = self.font.render('Score: ' + str(self.score), True, self.white)
        wpmText = self.font.render('wpm: ' + str(self.wpm), True, self.wpmColoring())
        textLength = self.font.render('Text Length: ' + str(len(self.textToWrite)) + ' chars', True, self.white)
        wordAmount = self.font.render('Words : ' + str(len(self.words)) + ' words', True, self.white)

        self.win.blit(self.bg, (0, 0))
        self.blitOutputText(self.textToWrite, (20, 400), self.white)
        self.blitOutputText(self.correctSentence, (20, 400), self.green)
        self.win.blit(inputText, (self.width / 2 - inputText.get_width() // 2, 600))
        self.win.blit(scoreText, (self.width - self.width / 4 - scoreText.get_width() // 2, 50))
        self.win.blit(timerText, (self.width - self.width / 4 - timerText.get_width() // 2, 80))
        self.win.blit(wpmText, (self.width / 2 - wpmText.get_width() // 2, 65))
        self.win.blit(textLength, (self.width / 4 - textLength.get_width() // 2, 50))
        self.win.blit(wordAmount, (self.width / 4 - wordAmount.get_width() // 2, 90))
        pygame.display.update()

    def drawResultWindow(self):
        inputText = self.font.render(self.writtenText, True, self.white)
        timerText = self.font.render('Timer: ' + str(self.timer), True, self.white)
        scoreText = self.font.render('Score: ' + str(self.score), True, self.white)
        wpmText = self.font.render('wpm: ' + str(self.wpm), True, self.wpmColoring())
        textLength = self.font.render('Text Length: ' + str(len(self.textToWrite)) + ' chars', True, self.white)
        wordAmount = self.font.render('Words : ' + str(len(self.words)) + ' words', True, self.white)
        insertText = self.font.render('Insert Your Username', True, self.white)
        submitText = self.font.render('Press [SPACE] To Submit', True, self.white)

        self.win.blit(self.bg, (0, 0))
        self.win.blit(inputText, (self.width / 2 - inputText.get_width() // 2, 600))
        self.win.blit(scoreText, (self.width - self.width / 4 - scoreText.get_width() // 2, 50))
        self.win.blit(timerText, (self.width - self.width / 4 - timerText.get_width() // 2, 80))
        self.win.blit(wpmText, (self.width / 2 - wpmText.get_width() // 2, 65))
        self.win.blit(textLength, (self.width / 4 - textLength.get_width() // 2, 50))
        self.win.blit(wordAmount, (self.width / 4 - wordAmount.get_width() // 2, 90))
        self.win.blit(insertText, (self.width / 2 - insertText.get_width() // 2, 550))
        self.win.blit(submitText, (self.width / 2 - submitText.get_width() // 2, 650))
        pygame.display.update()

    def run(self):
        self.clock.tick(60)
        self.countdown()
        self.startTime = time.time()
        run = True
        while run:
            self.redrawGameWindow()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if self.outputTextCharPos == len(self.textToWrite) and \
                        self.words[self.wordPosition] == self.writtenText:
                    self.score += 1
                    run = False

                if (event.type == pygame.KEYDOWN and pygame.key.get_mods() & pygame.KMOD_SHIFT) and \
                                                (event.key in range(pygame.K_a, pygame.K_z) or
                                                 event.key in list([pygame.K_COMMA, pygame.K_PERIOD, pygame.K_QUESTION,
                                                                    pygame.K_SEMICOLON, pygame.K_EXCLAIM,
                                                                    pygame.K_QUOTEDBL, pygame.K_QUOTE,
                                                                    pygame.K_BACKSPACE, pygame.K_SPACE,
                                                                    pygame.K_CAPSLOCK, pygame.KMOD_SHIFT])):
                    key = pygame.key.name(event.key).upper()
                    if key == "'":
                        key = '"'
                    elif key == ';':
                        key = ':'
                    self.rulesGame(key)

                elif event.type == pygame.KEYDOWN and (event.key in range(pygame.K_a, pygame.K_z) or
                                                event.key in list([pygame.K_COMMA, pygame.K_PERIOD, pygame.K_QUESTION,
                                                                   pygame.K_SEMICOLON, pygame.K_EXCLAIM,
                                                                   pygame.K_QUOTEDBL, pygame.K_QUOTE,
                                                                   pygame.K_BACKSPACE, pygame.K_SPACE,
                                                                   pygame.K_CAPSLOCK, pygame.KMOD_SHIFT,
                                                                   pygame.K_MINUS])):
                    key = pygame.key.name(event.key)
                    self.rulesGame(key)

                print(event)

            pygame.display.update()
        self.charPosition = 0
        return self.getUsername()

    def rulesGame(self, key):
        if key == 'backspace':
            self.backspaceIsPressed()

        elif key == 'space':
            self.spaceIsPressed()

        else:
            if self.inBounds():
                self.writtenText += key
                self.charPosition += 1
                self.outputTextCharPos += 1

    def rulesResult(self, key, run):
        if key == 'backspace':
            if self.charPosition > 0:
                self.charPosition -= 1
                self.writtenText = self.writtenText[:self.charPosition]
        elif key == 'space':
            if len(self.writtenText) != 0:
                run = False
        elif len(self.writtenText) < 13:
            self.writtenText += key
            self.charPosition += 1
        return run

    def backspaceIsPressed(self):
        if self.charPosition > 0:
            self.charPosition -= 1
            self.writtenText = self.writtenText[:self.charPosition]
            self.outputTextCharPos -= 1

    def spaceIsPressed(self):
        if self.writtenText == self.words[self.wordPosition]:
            self.writtenText = ''
            self.wordPosition += 1
            self.charPosition = 0
            self.score += 1
            if self.wordPosition != len(self.words):
                self.correctSentence += self.words[self.wordPosition-1] + ' '
            else:
                self.correctSentence += self.words[self.wordPosition-1]
        else:
            if self.charPosition != 0:
                self.writtenText += ' '
                self.charPosition += 1
            else:
                self.outputTextCharPos -= 1
        self.outputTextCharPos += 1

    def inBounds(self):
        return self.charPosition in range(0, len(self.words[self.wordPosition]))\
               and self.wordPosition in range(0, len(self.words))

    def time(self):
        self.timer = math.trunc(time.time() - self.startTime)

    def wordsPerMinute(self):
        if self.score != 0:
            self.wpm = math.trunc((self.score / self.timer) * 60)

    def wpmColoring(self):
        if self.wpm in range(1, 30):
            return self.green
        elif self.wpm in range(31, 61):
            return self.yellow
        elif self.wpm > 60:
            return self.red
        else:
            return self.white

    def countdown(self):
        countdownFont = pygame.font.SysFont(None, 120)
        for i in range(3, 0, -1):
            self.win.blit(self.bg, (0, 0))
            countdownText = countdownFont.render(str(i), True, self.white)
            self.win.blit(countdownText, (self.width / 2 - countdownText.get_width() // 2,
                                          self.height / 2 - countdownText.get_height() // 2))
            time.sleep(1)
            pygame.display.update()
        time.sleep(1)

    def getUsername(self):
        self.writtenText = ''
        run = True
        while run:
            self.drawResultWindow()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if (event.type == pygame.KEYDOWN and pygame.key.get_mods() & pygame.KMOD_SHIFT) and \
                        (event.key in range(pygame.K_a, pygame.K_z) or
                        event.key in range(pygame.K_0, pygame.K_9) or
                         event.key in list([pygame.K_BACKSPACE, pygame.K_SPACE, pygame.KMOD_SHIFT])):
                    key = pygame.key.name(event.key).upper()

                    run = self.rulesResult(key, run)

                elif event.type == pygame.KEYDOWN and (event.key in range(pygame.K_a, pygame.K_z) or
                        event.key in range(pygame.K_0, pygame.K_9) or
                        event.key in list([pygame.K_BACKSPACE, pygame.K_SPACE, pygame.KMOD_SHIFT])):
                    key = pygame.key.name(event.key)

                    run = self.rulesResult(key, run)

            pygame.display.update()
        return self.writtenText, self.wpm

    def blitOutputText(self, text, pos, color):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = self.font.size(' ')[0]  # The width of a space.
        maxWidth, maxHeight = self.win.get_size()
        wordHeight = 0
        x, y = pos
        for line in words:
            for word in line:
                wordSurface = self.font.render(word, True, color)
                wordWidth, wordHeight = wordSurface.get_size()
                if x + wordWidth >= maxWidth:
                    x = pos[0]  # Reset the x.
                    y += wordHeight  # Start on new row.
                self.win.blit(wordSurface, (x, y))
                x += wordWidth + space
            x = pos[0]  # Reset the x.
            y += wordHeight  # Start on new row.

    """
    def capsLockStatus(self):
        print(subprocess.check_output('xset q | grep 00:', shell=True))
        
        if subprocess.check_output('xset q | grep 00:', shell=True).split(" ")[4] == 'off':
            self.capsLkFlag = False
        if subprocess.check_output('xset q | grep 00:', shell=True).split(" ")[4] == 'on':
            self.capsLkFlag = True
        print("capslock ON is : ", self.capsLkFlag)"""
