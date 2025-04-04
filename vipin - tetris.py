import pygame
import random

pygame.font.init()

WIDTH, HEIGHT = 300, 600
BLOCK_SIZE = 30
COLS, ROWS = 10, 20
TOP_LEFT_X = 50
TOP_LEFT_Y = 50

# for the shapes
SHAPES = [
    [['.....','.....','..00.','.00..','.....'], ['.....','..0..','..00.','...0.','.....']],  # S
    [['.....','.....','.00..','..00.','.....'], ['.....','..0..','.00..','.0...','.....']],  # Z
    [['..0..','..0..','..0..','..0..','.....'], ['.....','0000.','.....','.....','.....']],  # I
    [['.....','.....','.00..','.00..','.....']],                                           # O
    [['.....','.0...','.000.','.....','.....'], ['.....','..00.','..0..','..0..','.....']],  # J
    [['.....','...0.','.000.','.....','.....'], ['.....','..0..','..0..','..00.','.....']],  # L
    [['.....','..0..','.000.','.....','.....'], ['.....','..0..','..00.','..0..','.....']]   # T
]
COLORS = [(0,255,0), (255,0,0), (0,255,255), (255,255,0), (255,165,0), (0,0,255), (128,0,128)]

class Piece:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = COLORS[SHAPES.index(shape)]
        self.rotation = 0

def create_grid(locked={}):
    return [[locked.get((j,i), (0,0,0)) for j in range(COLS)] for i in range(ROWS)]

def convert_shape(piece):
    positions = []
    format = piece.shape[piece.rotation % len(piece.shape)]
    for i, line in enumerate(format):
        for j, char in enumerate(line):
            if char == '0':
                positions.append((piece.x + j - 2, piece.y + i - 4))
    return positions

def valid_space(piece, grid):
    formatted = convert_shape(piece)
    return all((pos[0], pos[1]) in 
              [(j,i) for i in range(ROWS) for j in range(COLS) if grid[i][j] == (0,0,0)] 
              or pos[1] < 0 for pos in formatted)

def draw_grid(surface, grid):
    for i in range(ROWS):
        for j in range(COLS):
            pygame.draw.rect(surface, grid[i][j], 
                           (TOP_LEFT_X + j*BLOCK_SIZE, TOP_LEFT_Y + i*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)
    pygame.draw.rect(surface, (255,0,0), (TOP_LEFT_X, TOP_LEFT_Y, COLS*BLOCK_SIZE, ROWS*BLOCK_SIZE), 2)

def main(win):
    locked = {}
    grid = create_grid(locked)
    current_piece = Piece(5, 0, random.choice(SHAPES))
    clock = pygame.time.Clock()
    fall_time = 0
    run = True

    while run:
        grid = create_grid(locked)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time/1000 > 0.27:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid):
                current_piece.y -= 1
                for pos in convert_shape(current_piece):
                    if pos[1] > -1:
                        locked[pos] = current_piece.color
                current_piece = Piece(5, 0, random.choice(SHAPES))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and valid_space(Piece(current_piece.x-1, current_piece.y, current_piece.shape), grid):
                    current_piece.x -= 1
                if event.key == pygame.K_RIGHT and valid_space(Piece(current_piece.x+1, current_piece.y, current_piece.shape), grid):
                    current_piece.x += 1
                if event.key == pygame.K_DOWN and valid_space(Piece(current_piece.x, current_piece.y+1, current_piece.shape), grid):
                    current_piece.y += 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1

        shape_pos = convert_shape(current_piece)
        for x, y in shape_pos:
            if y > -1:
                grid[y][x] = current_piece.color

        win.fill((0,0,0))
        draw_grid(win, grid)
        pygame.display.update()

        if any(y < 0 for _, y in locked):
            run = False

    pygame.quit()

win = pygame.display.set_mode((400, 700))
pygame.display.set_caption('Tetris')
main(win)
