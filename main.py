import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 540, 600
WINDOW_SIZE = (WIDTH, HEIGHT)
CELL_SIZE = WIDTH // 9
GRID_SIZE = 9
FPS = 60

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)

# Set up the game window
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Sudoku Game")

# Set up the clock
clock = pygame.time.Clock()

# Sudoku grid
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Function to draw the grid
def draw_grid():
    for i in range(GRID_SIZE + 1):
        if i % 3 == 0:
            pygame.draw.line(window, BLACK, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 4)
            pygame.draw.line(window, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 4)
        else:
            pygame.draw.line(window, GRAY, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), 2)
            pygame.draw.line(window, GRAY, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), 2)

# Function to draw the numbers on the grid
def draw_numbers():
    font = pygame.font.SysFont(None, 48)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] != 0:
                number = font.render(str(grid[i][j]), True, BLACK)
                number_rect = number.get_rect(center=((j * CELL_SIZE) + CELL_SIZE // 2, (i * CELL_SIZE) + CELL_SIZE // 2))
                window.blit(number, number_rect)

# Function to check if the number can be placed at the given position
def is_valid(row, col, num):
    # Check if the number already exists in the same row
    for j in range(GRID_SIZE):
        if grid[row][j] == num:
            return False

    # Check if the number already exists in the same column
    for i in range(GRID_SIZE):
        if grid[i][col] == num:
            return False

    # Check if the number already exists in the same 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(row, col, num):
                        grid[row][col] = num
                        if solve_sudoku():
                            return True
                        grid[row][col] = 0
                return False
    return True

# Main game loop
def play_sudoku():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        window.fill(WHITE)
        draw_grid()
        draw_numbers()
        pygame.display.update()
        clock.tick(FPS)

# Start the game
solve_sudoku()
play_sudoku()
