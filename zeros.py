import pygame

pygame.init()
size_block = 200
margin = 15
width = height = size_block * 3 + margin * 4
blue = (0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0)

win = pygame.display.set_mode((width, height))

pygame.display.set_caption('Крестики нолики')

mas = [[0] * 3 for i in range(3)]
query = 0

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
            # query += 1
    for r in range(3):
        for c in range(3):
            x = c * size_block + (c + 1) * margin
            y = r * size_block + (r + 1) * margin
            pygame.draw.rect(win, white, (x, y, size_block, size_block))

            if mas[r][c] == 'x':
                pygame.draw.line(win, yellow, (x + 5, y + 5), (x + size_block - 5, y + size_block - 5), 8)
                pygame.draw.line(win, yellow, (x + size_block - 5, y + 5), (x + 5, y + size_block - 5), 8)
                query += 1
                print(query)
            elif mas[r][c] == 'o':
                pygame.draw.circle(win, blue, (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 8)
                query += 1
                print(query)
    pygame.display.update()