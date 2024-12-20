import random

import pygame
import math

from pygame import KEYDOWN

pygame.init()

FPS = 60

WIDTH, HEIGHT = 800,800
ROWS = 4
COLS = 4

RECT_HEIGHT = HEIGHT // COLS
RECT_WIDTH = WIDTH // ROWS

OUTLINE_COLOR = (187,173,160)
OUTLINE_THICKENS = 10
BACKGROUND_COLOR = (205,192,180)
FONT_COLOR = (119,110,101)

FONT = pygame.font.SysFont("comicsans", 60, bold=True)
MOVE_VEL = 20

WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("2048")

class Tile:
    COLORS = [
        (237, 229, 218),
        (238, 225, 201),
        (243, 178, 122),
        (246, 150, 101),
        (247, 124, 95),
        (247, 95, 59),
        (237, 208, 115),
        (237, 204, 99),
        (236, 202, 80),
    ]

    def __init__(self, value , row, col):
        self.value = value
        self.row = row
        self.col = col
        self.x = RECT_WIDTH * col
        self.y = RECT_HEIGHT * row

    def get_colors(self):
        color_index = int(math.log2(self.value) - 1)
        tile_color = self.COLORS[color_index]
        return tile_color

    def draw(self,window):
        color = self.get_colors()

        pygame.draw.rect(window, color, rect=(self.x,self.y,RECT_WIDTH,RECT_HEIGHT))

        text = FONT.render(str(self.value), 1 , FONT_COLOR)
        window.blit(
                text,
                (
                    self.x + (RECT_WIDTH / 2) - text.get_width() / 2,
                    self.y + (RECT_HEIGHT / 2) - text.get_height() / 2
                )
        )

    def move(self, delta):
        self.x += delta[0]
        self.y += delta[1]

    def set_position(self,ceil = False):
        if ceil:
            self.row = math.ceil(self.y / RECT_HEIGHT)
            self.col = math.ceil(self.x / RECT_WIDTH)
        else:
            self.row = math.floor(self.y / RECT_HEIGHT)
            self.col = math.floor(self.x / RECT_WIDTH)


def draw_grid(window):
    for row in range(1,ROWS):
        y = row * RECT_WIDTH
        pygame.draw.line(window, OUTLINE_COLOR, (y,0), (y, HEIGHT), OUTLINE_THICKENS  )

    for col in range(1, COLS):
        x = RECT_HEIGHT * col
        pygame.draw.line(window,OUTLINE_COLOR, (0,x), (WIDTH, x), OUTLINE_THICKENS)

    pygame.draw.rect(surface=window, color=OUTLINE_COLOR, rect=(0,0,WIDTH,HEIGHT), width=OUTLINE_THICKENS)

def draw(window, tiles):
    window.fill(BACKGROUND_COLOR)

    for tile in tiles.values():
        tile.draw(window)
    draw_grid(window)

    pygame.display.update()

def get_random_pos(tiles):
    row = None
    col = None
    while True:
        row = random.randrange(0, ROWS)
        col = random.randrange(0, COLS)

        if f"{row},{col}" not in tiles:
            break
    return row, col


def generate_tiles():
    tiles = {}
    for _ in range(2):
        row,col =  get_random_pos(tiles)
        tiles[f"{row},{col}"] = Tile(2,row,col)
    # print(tiles)
    # print(tiles.values())
    return tiles

def move_tiles(window, tiles, clock, direction):
    updated = True
    blocks = set()

    if direction == "left":
        sort_func = lambda x: x.col
        reverse = False
        delta = (-MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row},{tile.col - 1}")
        merge_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL
        move_check = lambda tile, next_tile: tile.x > next_tile.x + MOVE_VEL + RECT_WIDTH
        ceil = True

    elif direction == "right":
        sort_func = lambda x: x.col
        reverse = True
        delta = (MOVE_VEL, 0)
        boundary_check = lambda tile: tile.col == COLS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row},{tile.col + 1}")
        merge_check = lambda tile, next_tile: tile.x < next_tile.x - MOVE_VEL
        move_check = lambda tile, next_tile:tile.x + MOVE_VEL + RECT_WIDTH < next_tile.x
        ceil = False

    elif direction == "up":
        sort_func = lambda x: x.row
        reverse = False
        delta = (0,-MOVE_VEL)
        boundary_check = lambda tile: tile.row == 0
        get_next_tile = lambda tile: tiles.get(f"{tile.row - 1},{tile.col}")
        merge_check = lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL
        move_check = lambda tile, next_tile: tile.y > next_tile.y + MOVE_VEL + RECT_HEIGHT
        ceil = True

    elif direction == "down":
        sort_func = lambda x: x.row
        reverse = True
        delta = (0,MOVE_VEL)
        boundary_check = lambda tile: tile.row == ROWS - 1
        get_next_tile = lambda tile: tiles.get(f"{tile.row + 1},{tile.col}")
        merge_check = lambda tile, next_tile: tile.y < next_tile.y - MOVE_VEL
        move_check = lambda tile, next_tile:  tile.y + RECT_HEIGHT + MOVE_VEL < next_tile.y
        ceil = False

    while updated:
        clock.tick(FPS)
        updated = False
        sorted_tiles = sorted(tiles.values(), key=sort_func, reverse=reverse)

        for i, tile in enumerate(sorted_tiles):
            if boundary_check(tile):
                continue

            next_tile = get_next_tile(tile)
            if not next_tile:
                tile.move(delta)
            elif tile.value == next_tile.value and tile not in blocks and next_tile not in blocks:
                if merge_check(tile, next_tile):
                    tile.move(delta)
                else:
                    next_tile.value *= 2
                    sorted_tiles.pop(i)
                    blocks.add(next_tile)
            elif move_check(tile,next_tile):
                tile.move(delta)
            else:
                continue

            tile.set_position(ceil)
            updated = True

        update_tiles(window,tiles,sorted_tiles)

    return end_move(tiles)

def end_move(tiles):
    if len(tiles) == 16:
        return "lost"
    row, col = get_random_pos(tiles)
    tiles[f"{row},{col}"] = Tile(random.choice([2,4]), row, col)
    return "continue"

def update_tiles(window, tiles, sorted_tiles):
    tiles.clear()
    for tile in sorted_tiles:
        tiles[f"{tile.row},{tile.col}"] = tile
    draw(window,tiles)

def main(window):
    clock = pygame.time.Clock()
    run = True

    tiles = generate_tiles()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_tiles(window,tiles,clock,"left")
                if event.key == pygame.K_RIGHT:
                    move_tiles(window,tiles,clock,"right")
                if event.key == pygame.K_UP:
                    move_tiles(window,tiles,clock,"up")
                if event.key == pygame.K_DOWN:
                    move_tiles(window,tiles,clock,"down")

        draw(window,tiles)

    pygame.quit()

Tile(16,1,1)

if __name__ == "__main__":
    main(WINDOW)

