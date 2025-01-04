# Tetris Game

## Overview

This project is a graphical implementation of the classic game Tetris, built using Python and the Pygame library. Players manipulate falling blocks (tetrominoes) to form complete horizontal lines, which then disappear, scoring points. The game ends when the blocks stack up and reach the top of the playing area.

## Requirements

- Python 3.x
- Pygame library

## Installation

1.  **Install Python 3:** If you don't have Python 3 installed, download and install it from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2.  **Install Pygame:** Open a terminal or command prompt and run:

    ```bash
    pip install pygame
    ```

## How to Play

1.  **Clone the Repository (Optional):** If the code is hosted on a platform like GitHub, clone the repository:

    ```bash
    git clone <repository_url>
    ```

2.  **Navigate to the Directory:** In your terminal, navigate to the directory containing `tetris_game.py` (or where you cloned the repository).

3.  **Run the Game:** Execute the following command:

    ```bash
    python tetris_game.py
    ```

4.  **Controls:**
    *   **Left Arrow:** Move the tetromino left.
    *   **Right Arrow:** Move the tetromino right.
    *   **Down Arrow:** Soft drop (move the tetromino down faster).
    *   **Up Arrow:** Rotate the tetromino.

5.  **Objective:** Your goal is to clear as many lines as possible by strategically placing the falling tetrominoes. The game is over when the blocks stack to the top of the screen.

## Game Features

- Classic Tetris gameplay.
- Score tracking.
- "Next Piece" preview.
- Responsive controls.
- Visually appealing graphics.
- Increasing difficulty as more lines are cleared (speed increases).
- Game over screen.

## Potential Improvements

- **Hold Feature:** Allow the player to hold a piece for later use.
- **Ghost Piece:** Display a "ghost" piece showing where the current piece will land.
- **Line Clear Animation:** Add an animation effect for clearing lines.
- **Leveling System:** Implement a level system that increases speed and difficulty.
- **Advanced Scoring:** Award extra points for difficult moves (e.g., T-spins, clearing multiple lines).
- **Sound Effects:** Add sounds for actions like moving, rotating, clearing lines, and game over.
- **Music:** Add background music.
- **Start/Pause Menus:** Add menus for starting and pausing the game.
- **Enhanced Graphics:** Improve the visual style with images or more complex block designs.
- **AI Opponent:** Develop an AI that can play Tetris.
- **Customizable Controls:** Allow players to redefine key bindings.

## Code Structure

-   **`tetris_game.py`:** The main Python file containing the game code.
-   **`pygame.init()`:** Initializes Pygame.
-   **`display_score(score)`:** Displays the score.
-   **`draw_board(board)`:** Draws the Tetris board.
-   **`create_grid(locked_positions={})`:** Creates the grid representing the board state.
-   **`get_shape()`:** Returns a random tetromino.
-   **`valid_space(shape, x, y, board)`:** Checks if a move is valid.
-   **`check_lost(positions)`:** Checks for game over condition.
-   **`clear_rows(board, locked)`:** Clears full rows and updates the score.
-   **`draw_next_shape(shape, color)`:** Displays the next tetromino.
-   **`game_loop()`:** The main game loop, handling logic, events, and rendering.

## Contributing

Contributions to this project are welcome! If you find bugs, have suggestions for improvements, or want to add new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (Note: You should create a `LICENSE` file and choose a license if you haven't already).

## Acknowledgements

- Based on the classic Tetris game.
- Developed using the Pygame library.
- Thanks to the Python community for their resources and support.
