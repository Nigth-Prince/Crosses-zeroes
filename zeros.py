import time

import pygame

pygame.init()
size_block = 200
margin = 15
width = height = size_block * 3 + margin * 4
white = (255, 255, 255)
mas = [[0] * 3 for i in range(3)]
query = 0
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Крестики нолики')

sound = pygame.mixer.Sound('win.mp3')

def rules():
    pos = []
    for a in range(3):
        for b in range(3):
            pos.append(mas[a][b])
    for i in mas:
        if i == ['x', 'x', 'x']:
            sound.play()
            time.sleep(1)
            quit()
    if pos[::3] == ['x', 'x', 'x'] or pos[::-3] == ['x', 'x', 'x'] or pos[1:10:3] == ['x', 'x', 'x']\
            or pos[0:9:4] == ['x', 'x', 'x'] or pos[2:7:2] == ['x', 'x', 'x']:
        sound.play()
        time.sleep(1)
        quit()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (size_block + margin)
            row = y_mouse // (size_block + margin)

            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
            query += 1

    for r in range(3):
        for c in range(3):
            x = c * size_block + (c + 1) * margin
            y = r * size_block + (r + 1) * margin
            pygame.draw.rect(win, white, (x, y, size_block, size_block))

            if mas[r][c] == 'x':
                pygame.draw.line(win,(155,70,220), (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 8)
                pygame.draw.line(win, (70,220,155), (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 8)
            elif mas[r][c] == 'o':
                pygame.draw.circle(win, (220,155,70), (x + size_block // 2, y + size_block // 2),
                                   size_block // 2 - 3, 8)

    pygame.display.update()
    rules()