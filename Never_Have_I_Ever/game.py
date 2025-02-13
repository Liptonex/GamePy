import pygame
import random

# Open the file 'data.txt' in read mode and read all lines into a list
# file = open('database_PL.txt', 'r')  # Polish version
file = open('Never_Have_I_Ever/database.txt', 'r')  # English version
data = file.readlines()
file.close()

# Initialize Pygame
pygame.init()

# Set up the display window with a resizable screen of size 1900x1080
screen = pygame.display.set_mode((1900, 1080), pygame.RESIZABLE)  # Width, Height

# Set the title and icon for the application
pygame.display.set_caption("Never have I ever...")
icon = pygame.image.load("Never_Have_I_Ever/cheers.png")
pygame.display.set_icon(icon)

# Set the font for rendering text
font = pygame.font.Font('freesansbold.ttf', 54)

# Choose a random prompt from the data and remove it from the list
prompt = random.choice(data)
data.remove(prompt)
print(prompt)


def newPrompt():
    """
    Selects a new random prompt from the remaining data and removes it from the list.
    Also updates the global `prompt` variable.
    """
    global prompt
    prompt = random.choice(data)
    data.remove(prompt)


def renderTextCenteredAt(text, font, colour, x, y, screen, allowed_width):
    """
    Renders the given text centered at the specified (x, y) position on the screen.
    The text is automatically wrapped to fit within the allowed width.

    Args:
        text (str): The text to render.
        font (pygame.font.Font): The font to use for rendering.
        colour (tuple): The color of the text in RGB format.
        x (int): The x-coordinate for the center of the text.
        y (int): The y-coordinate for the top of the text.
        screen (pygame.Surface): The surface to render the text on.
        allowed_width (int): The maximum allowed width for the text.
    """
    # Split the text into words
    words = text.split()

    # Construct lines out of these words
    lines = []
    while len(words) > 0:
        # Get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # Add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    # Render each line below the last
    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # Calculate the top-left position of the font surface
        tx = x - fw / 2
        ty = y + y_offset

        # Render the line and blit it onto the screen
        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))

        # Update the y_offset for the next line
        y_offset += fh


def colorMix():
    """
    Generates a random RGB color with values between 50 and 255 for each channel.

    Returns:
        tuple: A tuple representing the RGB color.
    """
    x = random.randint(50, 255)
    y = random.randint(50, 255)
    z = random.randint(50, 255)
    return (x, y, z)


# Generate an initial random color
color = colorMix()

# Main game loop
running = True
while running:
    # Fill the screen with the current color
    screen.fill(color)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or pygame.K_RETURN:
                # Generate a new prompt and color when space or enter is pressed
                newPrompt()
                color = colorMix()

    # Render the current prompt centered on the screen
    renderTextCenteredAt(prompt, font, (0, 0, 0), 950, 500, screen, 1070)

    # Update the display
    pygame.display.update()
