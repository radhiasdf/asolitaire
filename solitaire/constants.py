import pygame as pg
from os.path import join

FPS = 60

SUITS = ['spades', 'clubs', 'hearts', 'diamonds']
VALUES = 13
PIXEL_SCALE = 3
size = pg.image.load(join('assets', 'card.png')).get_size()
CARD_SCALE = (size[0]*PIXEL_SCALE, size[1]*PIXEL_SCALE)
PILE_SPACING = 1*PIXEL_SCALE
EXTRA_PILE_SPACING = 5*PIXEL_SCALE
CARD_SPACING = 8*PIXEL_SCALE  # to show the numbers when theyre stacked face up
NUM_GROWING_PILES = 7

BOARD_SIZE = pg.Vector2(NUM_GROWING_PILES*(CARD_SCALE[0]+PILE_SPACING) + 2*(CARD_SCALE[0]+EXTRA_PILE_SPACING),
                        CARD_SCALE[1] + CARD_SPACING * (VALUES-1))

RANDOM_POP = [0, 5]

AUTO_WIN = False
