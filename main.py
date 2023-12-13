#importing needed libraries, files
import sys
import math
import pygame
import game

#RGB of needed colors
black = (0, 0, 0)
red = (253, 70, 89)
green = (100, 166, 74)
blue = (0, 0, 255)

#number of rows and columns
stolb = 7 #columns
ryad = 6 #rows

pole = game.create_pole()
game_over = False #for checking is game over
hid = 0

#initializing pygame
pygame.init()
kvadrat = 100 #square outside the circle
radius = int(kvadrat / 2 - 5) #radius of circle
width = stolb * kvadrat #width of screen
height = (ryad + 1) * kvadrat #height of screen
size = (width, height) #size of screen
screen = pygame.display.set_mode(size)
game.draw_pypole(pole) #call function draw.pypole
pygame.display.update() #updating display
myfont = pygame.font.SysFont("monospace", 55)

def anymat(pole, row, hid):
    d = 0
    k = 5
    z = row - 1
    if(hid == 0):
        d = 1
    if(hid == 1):
        d = 2
    while k != z:
            pole[k][col] = d
            game.draw_pypole(pole)
            pygame.time.wait(100)
            pole[k][col] = 0
            game.draw_pypole(pole)
            k = k - 1

while not game_over:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, black, (0, 0, width, kvadrat))
            posx = event.pos[0]
            pos2 = posx // 100
            if hid == 0:
                pygame.draw.circle(screen, red, (pos2 * int(kvadrat) + 50, int(kvadrat / 2)), radius)
            else:
                pygame.draw.circle(screen, green, (pos2 * int(kvadrat) + 50, int(kvadrat / 2)), radius)
        pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, black, (0, 0, width, kvadrat))

            if hid == 0:

                posx = event.pos[0]
                col= int(math.floor(posx/kvadrat))

                if pole[ryad - 1][col] != 0:
                    hid += 1
                    hid = hid % 2
                else:

                    row = game.Kudu_Monaradok(pole, col)
                    anymat(pole, row, hid)
                    game.drop_down(pole, row, col, 1)

                    if game.win(pole, 1):
                        label = myfont.render("!!RED!!", 1, red)
                        screen.blit(label, (40, 10))
                        game_over = True
                    if game.nichiya(pole):
                        label = myfont.render("!!!DRAW!!!", 1, blue)
                        screen.blit(label, (40, 10))
                        game_over = True

            else:

                posx = event.pos[0]
                col = int(math.floor(posx / kvadrat))

                if pole[ryad-1][col] != 0:
                    hid += 1
                    hid = hid % 2
                else:

                        row = game.Kudu_Monaradok(pole, col)
                        anymat(pole, row, hid)
                        game.drop_down(pole, row, col, 2)

                        if game.win(pole, 2):
                            label = myfont.render("!!!GREEN!!!", 1, green)
                            screen.blit(label, (40, 10))
                            game_over = True
                        if game.nichiya(pole):
                            label = myfont.render("DRAW", 1, blue)
                            screen.blit(label, (40, 10))
                            game_over = True

            game.print_pole(pole)
            game.draw_pypole(pole)
            hid += 1
            hid = hid % 2

            if game_over == True:
                pygame.time.wait(5000)

