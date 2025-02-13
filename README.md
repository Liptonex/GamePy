# GamePy

Repository of two games created using Python and Pygame library:
* Simple 2D game called Space Invaders: a classic shooter
* Never Have I Ever: a generator of prompts for the drinking game; works also on Android Python emulators 

# Never Have I Ever - PyGame Edition

<!-- ![Game Screenshot](screenshot.png) <!-- Add a screenshot if available -->

**Never Have I Ever** is a fun and interactive game built using Python and PyGame. It randomly displays prompts from a predefined list, allowing players to engage in the classic "Never Have I Ever" game digitally. The game features a dynamic background color changer and centered text rendering for a visually appealing experience.

---

## Features

- **Random Prompts**: The game selects random prompts from a text file (`data.txt`) and ensures no prompt is repeated.
- **Dynamic Background**: The background color changes randomly each time a new prompt is displayed.
- **Responsive Design**: The game window is resizable, making it adaptable to different screen sizes.
- **Centered Text Rendering**: Prompts are automatically wrapped and centered on the screen for better readability.
- **Keyboard Controls**: Press the **Spacebar** or **Enter** key to generate a new prompt.

---

## How to Play

1. **Install Dependencies**:
   Ensure you have Python and PyGame installed. You can install PyGame using pip:
   ```bash
   pip install pygame
   ```

2. **Customize the Prompt File**:
   The game comes with hundreds of preloaded prompts in the `database.txt` file, so you can start playing right away. If you'd like to add your own prompts or modify the existing ones, simply edit the `database.txt` file (one prompt per line). For example:
   ```
   Never have I ever traveled abroad.
   Never have I ever eaten sushi.
   Never have I ever gone skydiving.
   ```
   Feel free to personalize the game with your own creative prompts!


3. **Run the Game**:
   Execute the Python script to start the game:
   ```bash
   python never_have_i_ever.py
   ```

4. **Play**:
   - The game will display a random prompt.
   - Press **Spacebar** or **Enter** to get a new prompt.
   - Close the window to exit the game.

---

## Code Structure

- **`database.txt`**: Contains the list of prompts.
- **`never_have_i_ever.py`**: The main game script.
  - **`newPrompt()`**: Selects a new random prompt.
  - **`renderTextCenteredAt()`**: Renders text centered on the screen with automatic line wrapping.
  - **`colorMix()`**: Generates a random background color.
  - **Main Loop**: Handles events, updates the screen, and renders prompts.

---

## Customization

- **Prompts**: Edit `database.txt` to add or modify prompts.
- **Font**: Replace `freesansbold.ttf` with your preferred font file.
- **Icon**: Replace `cheers.png` with your own icon (64x64 recommended).
- **Screen Size**: Adjust the screen dimensions in `pygame.display.set_mode((1900, 1080), pygame.RESIZABLE)`.

---

## Requirements

- Python 3.x
- PyGame (`pip install pygame`)

---

<!-- ## Screenshots

<!-- Add screenshots here if available 
![Gameplay Screenshot](screenshot1.png)
![New Prompt Screenshot](screenshot2.png)

---


## Contributing

Contributions are welcome! If you'd like to improve the game, feel free to:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
-->
---

Enjoy the game and have fun playing **Never Have I Ever**! 🎉