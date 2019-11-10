import pygame

sentence = "once upon a time... There was a..."
word = sentence.split(" ")
inputText = ""

pygame.init()

clock = pygame.time.Clock()

x = 1200
y = 800

white = 255, 255, 255
red = 255, 0, 0, 50
green = 0, 255, 0, 50
blue = 0, 0, 255, 50
black = 0, 0, 0

capsLkFlag = False
shiftFlag = False

win = pygame.display.set_mode((x, y))
pygame.display.set_caption("Type Speed")
bg = pygame.image.load("typeracer_models/bg.png")

font = pygame.font.SysFont(None, 30)
text = font.render(sentence, True, white)
inputTxt = font.render(inputText, True, white)

# auga su kiekvienu tesingai irasytu zodziu
score = 0

# negali but zemiau 0 ir auksciau len(sentence)
charPosition = 0
wordPosition = 0
sentenceCPos = 0


def redrawGameWindow():
    win.blit(bg, (0, 0))
    win.blit(text, (x / 2 - text.get_width() // 2, 600))
    win.blit(inputTxt, (x / 2 - text.get_width() // 2, 700))
    #reiks naudot display_input funkcija, bet ja pertvarkyt
    #display_input_text(inputText, cPos, white)
    pygame.display.update()


def check_OutOfBounds(cPos, wPos):
    if cPos >= 0 and cPos < len(word[wPos]) and wPos >= 0 and wPos < len(word):
        return True
    return False


def coloring(char, color):
    win.fill(black)
    txt_surface = font.render(char, True, color)
    txt_box = txt_surface.get_rect(topleft=(x/2 - text.get_width() // 2, 200))
    win.blit(txt_surface, txt_box)
    pygame.display.update()


def display_input_text(string, pos, color):
    txt = ''
    if len(string) > 0:
        for c in string:
            #win.fill(bg)
            txt += c
            txt_surface = font.render(txt, True, color)
            txt_box = txt_surface.get_rect(topleft=(x/2 - text.get_width() // 2, 600))
            win.blit(txt_surface, txt_box)
            #pygame.display.update()
    else:
        #win.fill(bg)
        txt_surface = font.render(txt, True, color)
        txt_box = txt_surface.get_rect(topleft=(x / 2 - text.get_width() // 2, 600))
        win.blit(txt_surface, txt_box)
        #pygame.display.update()


def keyboard_control(inputTxt, cPos, wPos, senCPos):
    #print(key)
    #print('Sentence state ' + sentence[cPos])
    #print('Char Position: ' + str(cPos))
#kiekviena if isskirtyti i naujas funkcijas ir parasyt rules atskiras funkcijas !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if event.key == pygame.K_BACKSPACE:
        if cPos > 0:
            cPos -= 1
            inputTxt = inputTxt[:cPos]
            #display_input_text(inputTxt, cPos, white)  # TVARKYTI SPALVAS VISUR

    elif event.key == pygame.K_SPACE:
        if inputTxt == word[wPos]:

            #display_input_text(inputTxt, cPos, black)  # Tvarkyt spalvas
            inputTxt = ""
            wPos += 1
            cPos = 0
        else:
            if cPos != 0:
                inputTxt += " "
                display_input_text(inputTxt, cPos + 1, white) # Tvarkyt spalvas
                cPos += 1

    else:
        if check_OutOfBounds(cPos, wPos):
            inputTxt += key
            if key == word[wPos][cPos]:
                pass
                #print(sentence[cPos])
                #display_input_text(inputTxt, cPos, white)
                #coloring(sentence[senCPos], green)
            else:
                pass
                #display_input_text(inputTxt, cPos, white)
                #coloring(sentence[senCPos], red)
            cPos += 1
    senCPos += 1

    return inputTxt, cPos, wPos, senCPos


run = True
while run:
    #pygame.time.delay(10)

    redrawGameWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if (event.type == pygame.KEYDOWN and pygame.key.get_mods() & pygame.KMOD_SHIFT) and \
                                            (event.key in range(pygame.K_a, pygame.K_z) or
                                             event.key in list([pygame.K_COMMA, pygame.K_PERIOD, pygame.K_QUESTION,
                                                                pygame.K_COLON, pygame.K_EXCLAIM, pygame.K_QUOTEDBL,
                                                                pygame.K_QUOTE, pygame.K_BACKSPACE, pygame.K_SPACE,
                                                                pygame.K_CAPSLOCK, pygame.KMOD_SHIFT])):
            key = pygame.key.name(event.key).upper()
            #print("UPPER")
            inputText, charPosition, wordPosition, sentenceCPos = keyboard_control(inputText, charPosition, wordPosition, sentenceCPos)

        elif event.type == pygame.KEYDOWN and (event.key in range(pygame.K_a, pygame.K_z) or
                                               event.key in list([pygame.K_COMMA, pygame.K_PERIOD, pygame.K_QUESTION,
                                                                  pygame.K_COLON, pygame.K_EXCLAIM, pygame.K_QUOTEDBL,
                                                                  pygame.K_QUOTE, pygame.K_BACKSPACE, pygame.K_SPACE,
                                                                  pygame.K_CAPSLOCK, pygame.KMOD_SHIFT])):
            key = pygame.key.name(event.key)
            #print("LOWER")
            inputText, charPosition, wordPosition, sentenceCPos = keyboard_control(inputText, charPosition, wordPosition, sentenceCPos)

        print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()