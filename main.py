import pygame


def inter(x1, y1, x2, y2, db1, db2):
    if x1 > x2 - db1 and x1 < x2 + db2 and y1 > y2 - db1 and y1 < y2 + db2:
        return 1
    else:
        return 0


pygame.init()
window = pygame.display.set_mode((700, 700))
screen = pygame.Surface((700, 700))
player = pygame.Surface((40, 40))
celi = pygame.Surface((40, 40))
arrow = pygame.Surface((20, 40))

img_a = pygame.image.load("a.png")
img_z = pygame.image.load("z.png")
img_s = pygame.image.load("s.png")

a_x = 1000
a_y = 1000
strike = False
count = 0
player.set_colorkey((0, 0, 0))
arrow.set_colorkey((0, 0, 0))
celi.set_colorkey((0, 0, 0))
myfont = pygame.font.SysFont("monospace", 20)

z_x = 0
z_y = 0
right = True
x_p = 0
y_p = 660
done = False
while done == False:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            y_p += 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            y_p -= 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            x_p -= 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            x_p += 10
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            if strike == False:
                strike = True
                a_x = x_p
                a_y = y_p - 40
    if strike:
        a_y -= 0.5
        if a_y < 0:
            strike = False
            a_y = 1000
            a_x = 1000
    if inter(a_x, a_y, z_x, z_y, 20, 40):
        count += 1
        strike = False
        a_y = 1000
        a_x = 1000
    if right:
        z_x += 0.5
        if z_x > 690:
            z_x -= 0.5
            right = False
    else:
        z_x -= 0.5
        if z_x < 0:
            z_x += 0.5
            right = True

    screen.fill((219, 112 , 147 ))
    string = myfont.render("Point:" + str(count), 0, (0, 0, 128))
    screen.blit(string, (0, 50))
    arrow.blit(img_a, (0, 0))
    player.blit(img_s, (0, 0))
    celi.blit(img_z, (0, 0))
    screen.blit(celi, (z_x, z_y))
    screen.blit(arrow, (a_x, a_y))
    screen.blit(player, (x_p, y_p))
    window.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()
