import pygame
import random

# file = open('database_PL.txt', 'r')  # Wersja PL
file = open('data.txt', 'r')  # Wersja ENG

data = file.readlines()
file.close()

# INIT!
pygame.init()
# Background
screen = pygame.display.set_mode((1900, 1080), pygame.RESIZABLE)  # Width, Height

# Title and icon
pygame.display.set_caption("Never have I ever...")
icon = pygame.image.load("cheers.png")
pygame.display.set_icon(icon)

# Font
font = pygame.font.Font('freesansbold.ttf', 54)
prompt = random.choice(data)
data.remove(prompt)
print(prompt)


def newPrompt():
    global prompt
    prompt = random.choice(data)
    data.remove(prompt)


# def showPrompt():
#     score = font.render(prompt, True, (0, 0, 0))
#     screen.blit(score, (300, 300))

def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # now we've split our text into lines that fit into the width, actually
    # render them

    # we'll render each line below the last, so we need to keep track of
    # the culmative height of the lines we've rendered so far
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        y_offset += fh


def colorMix():
    x = random.randint(50, 255)
    y = random.randint(50, 255)
    z = random.randint(50, 255)
    all = [x, y, z]
    return tuple(all)


color = colorMix()

running = True
while running:
    screen.fill(color)
    # screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or pygame.K_RETURN:
                newPrompt()
                color = colorMix()
    renderTextCenteredAt(prompt, font, (0, 0, 0), 950, 500, screen, 1070)
    pygame.display.update()
