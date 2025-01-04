import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
orange = (255, 165, 0)

# Game settings
display_width = 800
display_height = 600
block_size = 30
board_width = 10  # in blocks
board_height = 20  # in blocks
board_x = (display_width - board_width * block_size) // 2
board_y = (display_height - board_height * block_size) // 2
fall_speed = 1 # initial falling speed

font_style = pygame.font.SysFont(None, 25)

# Tetromino shapes
shapes = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 0, 0], [1, 1, 1]],  # T
    [[0, 0, 1], [1, 1, 1]],  # J
    [[1, 0, 0], [1, 1, 0], [1, 0, 0]], # L
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]  # Z
]

shape_colors = [cyan, yellow, magenta, blue, orange, green, red]

# Initialize the display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tetris')

clock = pygame.time.Clock()

def display_score(score):
    """Displays the score on the screen."""
    value = font_style.render("Score: " + str(score), True, white)
    game_display.blit(value, [0, 0])

def draw_board(board):
    """Draws the Tetris board."""
    for y, row in enumerate(board):
        for x, value in enumerate(row):
            if value:
                pygame.draw.rect(game_display, shape_colors[value - 1],
                                 [board_x + x * block_size, board_y + y * block_size, block_size, block_size])
                pygame.draw.rect(game_display, white,
                                 [board_x + x * block_size, board_y + y * block_size, block_size, block_size], 1)

def create_grid(locked_positions={}):
    """Creates the grid for the board."""
    grid = [[0 for _ in range(board_width)] for _ in range(board_height)]
    for y in range(board_height):
        for x in range(board_width):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

def get_shape():
    """Returns a random Tetromino shape and color."""
    shape_index = random.randint(0, len(shapes) - 1)
    return shapes[shape_index], shape_colors[shape_index], shape_index + 1

def valid_space(shape, x, y, board):
    """Checks if the current shape position is valid on the board."""
    for i, row in enumerate(shape):
        for j, value in enumerate(row):
            if value:
                if not (0 <= x + j < board_width and 0 <= y + i < board_height):
                    return False
                if board[y + i][x + j]:
                    return False
    return True

def check_lost(positions):
    """Checks if the player has lost (blocks stacked to the top)."""
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def clear_rows(board, locked):
    """Clears completed rows and returns the number of rows cleared."""
    inc = 0
    for i in range(len(board) - 1, -1, -1):
        row = board[i]
        if 0 not in row:
            inc += 1
            # remove locked positions
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < i:
                newKey = (x, y + inc)
                locked[newKey] = locked.pop(key)
    return inc

def draw_next_shape(shape, color):
    """Draws the next shape in the designated area."""
    font = pygame.font.SysFont(None, 30)
    label = font.render('Next Shape', 1, white)

    sx = board_x + board_width * block_size + 50
    sy = board_y + board_height * block_size // 2 - 100
    
    game_display.blit(label, (sx + 10, sy - 30))
    
    for i, line in enumerate(shape):
        row = list(line)
        for j, column in enumerate(row):
            if column == 1:
                pygame.draw.rect(game_display, color, (sx + j * block_size, sy + i * block_size, block_size, block_size), 0)
                pygame.draw.rect(game_display, white, (sx + j * block_size, sy + i * block_size, block_size, block_size), 1)

def game_loop():
    """Main game loop."""
    global fall_speed
    locked_positions = {}
    board = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece, current_color, current_piece_value = get_shape()
    next_piece, next_color, next_piece_value = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    score = 0

    x = board_width // 2 - 2  # Starting position
    y = 0

    while run:
        board = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        # Piece falling logic
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            y += 1
            if not valid_space(current_piece, x, y, board) and y > 0:
                y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x -= 1
                    if not valid_space(current_piece, x, y, board):
                        x += 1
                elif event.key == pygame.K_RIGHT:
                    x += 1
                    if not valid_space(current_piece, x, y, board):
                        x -= 1
                elif event.key == pygame.K_DOWN:
                    y += 1
                    if not valid_space(current_piece, x, y, board):
                        y -= 1
                elif event.key == pygame.K_UP:
                    # Rotate shape
                    current_piece = list(zip(*current_piece[::-1]))
                    if not valid_space(current_piece, x, y, board):
                      # Try to find a valid space for the rotated piece
                      valid_rotation = False
                      for offset in range(1, len(current_piece) + 1):
                        # Try moving left and right
                        if valid_space(current_piece, x - offset, y, board):
                          x -= offset
                          valid_rotation = True
                          break
                        elif valid_space(current_piece, x + offset, y, board):
                          x += offset
                          valid_rotation = True
                          break
                      if not valid_rotation:
                        # Revert rotation if no valid position is found
                        for _ in range(3):
                          current_piece = list(zip(*current_piece[::-1]))

        # Draw the current piece
        for i, row in enumerate(current_piece):
            for j, value in enumerate(row):
                if value:
                    pygame.draw.rect(game_display, current_color,
                                     [board_x + (x + j) * block_size, board_y + (y + i) * block_size, block_size, block_size])
                    pygame.draw.rect(game_display, white,
                                     [board_x + (x + j) * block_size, board_y + (y + i) * block_size, block_size, block_size], 1)

        # Add piece to the grid when it lands
        if change_piece:
            for i, row in enumerate(current_piece):
                for j, value in enumerate(row):
                    if value:
                        locked_positions[(x + j, y + i)] = current_piece_value
            current_piece = next_piece
            current_color = next_color
            current_piece_value = next_piece_value
            next_piece, next_color, next_piece_value = get_shape()
            x = board_width // 2 - 2
            y = 0
            change_piece = False
            score += clear_rows(board, locked_positions) * 10
            if clear_rows(board, locked_positions) >= 4: # increase speed after clearing 4 lines
              fall_speed *= 0.95

        draw_board(board)
        draw_next_shape(next_piece, next_color)
        display_score(score)

        # Draw grid lines
        for i in range(board_height):
            pygame.draw.line(game_display, white, (board_x, board_y + i * block_size),
                             (board_x + board_width * block_size, board_y + i * block_size))
            for j in range(board_width):
                pygame.draw.line(game_display, white, (board_x + j * block_size, board_y),
                                 (board_x + j * block_size, board_y + board_height * block_size))

        # Draw border around the board
        pygame.draw.rect(game_display, red, (board_x - 2, board_y - 2, board_width * block_size + 4, board_height * block_size + 4), 4)

        if check_lost(locked_positions):
            run = False

        pygame.display.update()
        game_display.fill(black)

    # Game over message
    font = pygame.font.SysFont(None, 60)
    label = font.render('You Lost!', 1, white)
    game_display.blit(label, (display_width / 2 - label.get_width() / 2, display_height / 2 - label.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(2000)  # Wait for 2 seconds before quitting

game_loop()