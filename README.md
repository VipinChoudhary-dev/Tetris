This project is a Python-based recreation of the classic Tetris game, designed to simulate the original mechanics while also serving as a hands-on learning exercise in game development and UI design. Built using the Pygame library, this game focuses on the fundamental logic behind tile-based puzzles, real-time user interaction, and dynamic game progression.


🎯 Objective :

The goal of the game is simple: strategically rotate and place falling tetromino blocks (shaped like L, I, T, etc.) to create complete horizontal lines. When a full line is completed, it disappears, and the player earns points. The game continues until the stacked blocks reach the top of the screen, triggering a game over.

🔧 Technologies Used :

  1) Python: The core programming language used to build the game logic and manage the game loop.
  2) Pygame: A Python library used for 2D game development, handling rendering, events, input, and time-based functions.
  3) Random: To generate different types of tetromino shapes in random order, simulating unpredictability in gameplay.

⚙️ Key Features :

1) Falling Tetrominoes :
The game uses a set of pre-defined shapes (tetrominoes) that fall from the top of the screen. The pieces drop at regular intervals and increase in speed as the player progresses, simulating increasing difficulty.

2) Collision Detection :
The game checks for collision with the boundaries, the floor, and already placed blocks to prevent overlapping and ensure accurate movement.

3) Line Clearing and Scoring :
When a horizontal line is filled with blocks, it gets cleared and the blocks above drop down. The player is rewarded with points for each line cleared.

4) Game Over and Restart :
The game ends when the stack of blocks reaches the top. A "Game Over" message is displayed, and players have the option to restart the game.

5) User Input Handling :
The game is fully interactive with keyboard controls allowing players to move, rotate, and drop blocks using arrow keys and special keys like spacebar.
