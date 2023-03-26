import pygame as pg

W = 600
H = 600
w = W // 7
h = H // 7
x = 0
y = H // 2 - H // 2
FPS = 60


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 255, 0)
PINK = (230, 50, 230)
BIR = (162, 80, 255)

rad = 50

values = {'x1': 130, 'x2': 190, 'x3': 250, 'x4': 310, 'x5': 370,
          'y1': 180, 'y2': 240, 'y3': 300, 'y4': 360, 'y5': 420, 'dir4': 'right'}

pg.init()
win = pg.display.set_mode((W, H))
pg.display.set_caption("Крестики - нолики")
fps = pg.time.Clock()
list = {1: (100,100), 2: (300,100), 3: (500,100), 4: (100,300), 5: (300,300),
        6: (500,300), 7: (100,500), 8: (300,500), 9: (500,500)}
left  = [(0,0), (200,100), (400,100)]
right = [(200,100), (400,100)]
win.fill(WHITE)
f = 0
l = 1
while True:

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            for mouse in position:
                f += 1
                if i.pos > mouse and i.pos < position[f+1]:

                    if i.button == 1: # отрисовка круга
                        pg.draw.circle(win, (250,170,20), list[1], 80, 5, False)

                    elif i.button == 3: # kpectik
                        pg.draw.line(win, (200, 100, 70), (i.pos[0] - 90,i.pos[1] - 90), (i.pos[0] + 90, i.pos[1] + 90))
                        pg.draw.line(win, (200, 100, 70), (i.pos[0] - 90,i.pos[1] + 90), (i.pos[0] + 90, i.pos[1] - 90))
                        print(i.pos)
                        pg.display.update()
                else: pass
                l += 1
    pg.draw.line(win, (0, 0, 0), (H // 3,0), (H // 3, W))
    pg.draw.line(win, (0, 0, 0), (H // 3 * 2,0), (H // 3 * 2, W))
    pg.draw.line(win, (0, 0, 0), (0, W // 3), (H, W // 3))
    pg.draw.line(win, (0, 0, 0), (0, W // 3 * 2), (H, W // 3 * 2))

    pg.display.update()
    fps.tick(FPS)
