import sys
import math
import numpy as np
import pygame


black = (0, 0, 0)
blue = (0, 0, 255)
red = (253, 70, 89)
green = (100, 166, 74)

stolb = 7
ryad = 6


def create_pole():
    pole = np.zeros((ryad, stolb))
    return pole

def drop_down(pole, row, col, piece):
    pole[row][col] = piece

def Kudu_Monaradok(pole, Kol):
    for r in range(ryad):
        if pole[r][Kol] == 0:
            return r


def print_pole(pole):

    np.flip(pole, 0)

def nichiya(pole):
    l = 0
    for s in range(7):
        for r in range(6):
            if (pole[r][s] == 1 or pole[r][s] == 2):
                l = l + 1
    if(l == 42):
        return True

def win(pole, piece):

    for s in range(stolb - 3):
        for r in range(ryad):
            if pole[r][s] == piece and pole[r][s+1] == piece and pole[r][s+2] == piece and pole[r][s+3] == piece:
                return True
    # Vertical check
    for s in range(stolb):
        for r in range(ryad - 3):
            if pole[r][s] == piece and pole[r+1][s] == piece and pole[r+2][s] == piece and pole[r+3][s] == piece:
                return True

    for s in range(stolb - 3):
        for r in range(ryad - 3):
            if pole[r][s] == piece and pole[r+1][s+1] == piece and pole[r+2][s+2] == piece and pole[r+3][s+3] == piece:
                return True

    for s in range(stolb - 3):
        for r in range(3, ryad):
            if pole[r][s] == piece and pole[r-1][s+1] == piece and pole[r-2][s+2] == piece and pole[r-3][s+3] == piece:
                return True


def draw_pypole(pole):

    for s in range(stolb):
        for r in range(ryad):
            pygame.draw.rect(screen, blue, (s * kvadrat, r * kvadrat + kvadrat, kvadrat, kvadrat))
            pygame.draw.circle(screen, black, (int(s * kvadrat + kvadrat / 2), int(r * kvadrat + kvadrat + kvadrat / 2)), radius)

    for s in range(stolb):
        for r in range(ryad):
                if pole[r][s] == 1:
                    pygame.draw.circle(screen, red, (int(s * kvadrat + kvadrat / 2), height - int(r * kvadrat + kvadrat / 2)), radius)
                elif pole[r][s] == 2:
                    pygame.draw.circle(screen, green, (int(s * kvadrat + kvadrat / 2), height - int(r * kvadrat + kvadrat / 2)), radius)
    pygame.display.update()

pole = create_pole()

kvadrat = 100
radius = int(kvadrat / 2 -5)
width = stolb * kvadrat
height = (ryad + 1) * kvadrat
size = (width, height)
screen = pygame.display.set_mode(size)