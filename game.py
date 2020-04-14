import pygame
from config import one

a = one()
pygame.init()

screen_width = 800
screen_length = 800
win = pygame.display.set_mode((screen_length, screen_width))
pygame.display.set_caption(a.c1)

walkRight = [pygame.image.load('R1.png'), pygame.image.load('./R2.png')]
walkRight.append(pygame.image.load('R3.png'))
walkRight.append(pygame.image.load('R4.png'))
walkRight.append(pygame.image.load('R5.png'))
walkRight.append(pygame.image.load('R6.png'))
walkRight.append(pygame.image.load('R7.png'))
walkRight.append(pygame.image.load('R8.png'))
walkRight.append(pygame.image.load('R9.png'))
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png')]
walkLeft.append(pygame.image.load('L3.png'))
walkLeft.append(pygame.image.load('L4.png'))
walkLeft.append(pygame.image.load('L5.png'))
walkLeft.append(pygame.image.load('L6.png'))
walkLeft.append(pygame.image.load('L7.png'))
walkLeft.append(pygame.image.load('L8.png'))
walkLeft.append(pygame.image.load('L9.png'))
bg = pygame.image.load('grass.png')
bg = pygame.transform.scale(bg, (screen_length, screen_width))
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()
score1 = 0
score2 = 0
timer = 30
dt = 0
level_a = 1
level_b = 1

# Creating the class for the player


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.visible = True
        self.hitbox = (self.x + 20, self.y, 28, 60)

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(char, (self.x, self.y))

        self.hitbox = (self.x + 20, self.y, 28, 60)
#        pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.visible = False
        player2.visible = True
        self.x = player1_initial[0]
        self.y = player1_initial[1] + 50
        timer = 30


class playernew(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.visible = False
        self.hitbox = (self.x + 20, self.y, 28, 60)

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(char, (self.x, self.y))

        self.hitbox = (self.x + 20, self.y, 28, 60)
#        pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def hit(self):
        self.visible = False
        player1.visible = True
        self.x = player2_initial[0]
        self.y = player2_initial[1]
        timer = 30


class enemya(object):
    picture = [pygame.image.load('dude.png')]

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 3, self.y + 4, 60, 40)
        self.flag_a = True
        self.flag_b = True

    def draw(self, win):
        win.blit(self.picture[0], (self.x, self.y))
#       pygame.draw.rect(win, (255,0,0), self.hitbox,2)


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png')]
    walkRight.append(pygame.image.load('R3E.png'))
    walkRight.append(pygame.image.load('R4E.png'))
    walkRight.append(pygame.image.load('R5E.png'))
    walkRight.append(pygame.image.load('R6E.png'))
    walkRight.append(pygame.image.load('R7E.png'))
    walkRight.append(pygame.image.load('R8E.png'))
    walkRight.append(pygame.image.load('R9E.png'))
    walkRight.append(pygame.image.load('R10E.png'))
    walkRight.append(pygame.image.load('R11E.png'))
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png')]
    walkLeft.append(pygame.image.load('L3E.png'))
    walkLeft.append(pygame.image.load('L4E.png'))
    walkLeft.append(pygame.image.load('L5E.png'))
    walkLeft.append(pygame.image.load('L6E.png'))
    walkLeft.append(pygame.image.load('L7E.png'))
    walkLeft.append(pygame.image.load('L8E.png'))
    walkLeft.append(pygame.image.load('L9E.png'))
    walkLeft.append(pygame.image.load('L10E.png'))
    walkLeft.append(pygame.image.load('L11E.png'))

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.path = [x, end]
        self.walkCount = 0
        if player1.visible:
            self.vel = 3*level_a
        if player2.visible:
            self.vel = 3*level_b
        self.flag_a = True
        self.flag_b = True
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0

        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1

        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
#        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x < self.path[1] + self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:
            if self.x > self.path[0] - self.vel:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0


def redrawGameWindow():
    win.blit(bg, (0, 0))

#   This is initializing all the players and the obstacles
    player1.draw(win)
    player2.draw(win)
    goblin1.draw(win)
    goblin2.draw(win)
    goblin3.draw(win)
    goblin4.draw(win)
    goblin5.draw(win)
    goblin6.draw(win)
    goblin7.draw(win)
    goblin8.draw(win)
    goblin9.draw(win)
    goblin10.draw(win)
    goblin11.draw(win)
    goblin12.draw(win)
    goblin13.draw(win)
    goblin14.draw(win)
    goblin15.draw(win)
    dude1.draw(win)
    dude2.draw(win)
    dude3.draw(win)
    dude4.draw(win)
    dude5.draw(win)
    dude6.draw(win)
    dude7.draw(win)
    dude8.draw(win)
    dude9.draw(win)
    dude10.draw(win)
    dude11.draw(win)
    dude12.draw(win)
    dude13.draw(win)
    dude14.draw(win)
    dude15.draw(win)

#   This is making the score and the fonts for the score
    sc = f.render(a.c2 + str(score1), 1, a.color1)
    sc2 = f.render(a.c3 + str(score2), 1, a.color1)
    ti = f.render(a.c4 + str(timer), 4, a.color2)
    li_a = f.render(a.c5 + str(level_a), 3, a.color3)
    li_b = f.render(a.c6 + str(level_b), 3, a.color3)

    win.blit(ti, (490, 10))
    if player1.visible:
        win.blit(sc, (200, 10))
        win.blit(li_a, ((0, 740)))
    if player2.visible:
        win.blit(sc2, (200, 10))
        win.blit(li_b, ((0, 740)))

    pygame.display.update()

#   The initializing of the players with the positions
player1_initial = [360, 690]
player2_initial = [360, 0]


player1 = player(360, 740, 64, 64)
player2 = playernew(360, 0, 64, 64)


dude1 = enemya(0, 690, 80, 80)
goblin1 = enemy(50, 670, 80, 80, 250)
dude2 = enemya(280, 690, 80, 80)
goblin2 = enemy(350, 670, 80, 80, 550)
dude3 = enemya(600, 690, 80, 80)
goblin3 = enemy(650, 670, 80, 80, 750)


goblin4 = enemy(0, 530, 80, 80, 150)
dude4 = enemya(200, 550, 80, 80)
goblin5 = enemy(250, 530, 80, 80, 450)
dude5 = enemya(500, 550, 80, 80)
goblin6 = enemy(550, 530, 80, 80, 700)
dude6 = enemya(750, 550, 80, 80)


dude7 = enemya(0, 390, 80, 80)
goblin7 = enemy(50, 370, 80, 80, 250)
dude8 = enemya(280, 390, 80, 80)
goblin8 = enemy(350, 370, 80, 80, 550)
dude9 = enemya(600, 390, 80, 80)
goblin9 = enemy(650, 370, 80, 80, 750)


goblin10 = enemy(0, 230, 80, 80, 150)
dude10 = enemya(200, 250, 80, 80)
goblin11 = enemy(250, 230, 80, 80, 450)
dude11 = enemya(500, 250, 80, 80)
goblin12 = enemy(550, 230, 80, 80, 700)
dude12 = enemya(750, 250, 80, 80)


dude13 = enemya(0, 90, 80, 80)
goblin13 = enemy(50, 110, 80, 80, 250)
dude14 = enemya(280, 90, 80, 80)
goblin14 = enemy(350, 110, 80, 80, 550)
dude15 = enemya(600, 90, 80, 80)
goblin15 = enemy(650, 110, 80, 80, 750)

goblins = [goblin1, goblin2]
goblins.append(goblin3)
goblins.append(goblin4)
goblins.append(goblin5)
goblins.append(goblin6)
goblins.append(goblin7)
goblins.append(goblin8)
goblins.append(goblin9)
goblins.append(goblin10)
goblins.append(goblin11)
goblins.append(goblin12)
goblins.append(goblin13)
goblins.append(goblin14)
goblins.append(goblin15)
obstacles = [dude1, dude2]
obstacles.append(dude3)
obstacles.append(dude4)
obstacles.append(dude5)
obstacles.append(dude6)
obstacles.append(dude7)
obstacles.append(dude8)
obstacles.append(dude9)
obstacles.append(dude10)
obstacles.append(dude11)
obstacles.append(dude12)
obstacles.append(dude13)
obstacles.append(dude14)
obstacles.append(dude15)

# These are all the global variables that are being used
run = True
f = pygame.font.SysFont(a.c10, 30, True)
f1 = pygame.font.SysFont(a.c10, 45, True)
timer_flag = False
count1 = 0
count2 = 0
l_inc_a = 0
l_inc_b = 0
life_a = True
life_b = True

# This is the endscreen that will output the result of the winner


def endscreen():
    win.blit(bg, (0, 0))
    sc = f1.render(a.c7, 1, a.color1)
    sc2 = f1.render(a.c8, 1, a.color1)
    sc3 = f1.render(a.c9, 1, a.color1)
    if score1 > score2:
        win.blit(sc, (200, 400))
    else:
        if score2 > score1:
            win.blit(sc2, (200, 400))
        else:
            win.blit(sc3, (200, 400))
    pygame.display.update()
    run = False
# This is the main game loop
while run:
    clock.tick(27)

    timer = int(timer - dt)
    dt = clock.tick(10000000) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    check1 = player1.vel - player1.width // player1.vel - 15
    if keys[pygame.K_LEFT] and player1.x > check1:
        player1.x -= player1.vel
        player1.left = True
        player1.right = False

    check2 = screen_width - player1.vel - player1.width
    if keys[pygame.K_RIGHT] and player1.x < check2:
        player1.x += player1.vel
        player1.left = False
        player1.right = True

    check3 = player1.vel - player1.height//player1.vel
    if keys[pygame.K_UP] and player1.y > check3:
        player1.y -= player1.vel
        player1.left = False
        player1.right = False
        player1.walkCount = 0

    check4 = screen_length - player1.height - player1.vel
    if keys[pygame.K_DOWN] and player1.y < check4:
        player1.y += player1.vel
        left = False
        right = False
        walkCount = 0

    check5 = player2.vel - player2.width // player2.vel - 15
    if keys[pygame.K_a] and player2.x > check5:
        player2.x -= player2.vel
        player2.left = True
        player2.right = False

    check6 = screen_width - player2.vel - player2.width
    if keys[pygame.K_d] and player2.x < check6:
        player2.x += player2.vel
        player2.left = False
        player2.right = True

    check7 = screen_length - player2.height - player2.vel
    if keys[pygame.K_s] and player2.y < check7:
        player2.y += player1.vel
        player2.left = False
        player2.right = False
        player2.walkCount = 0

    check8 = player2.vel - player2.height // player2.vel
    if keys[pygame.K_w] and player2.y > check8:
        player2.y -= player2.vel
        left = False
        right = False
        walkCount = 0

    for goblin in goblins:
        if player1.y + player1.height < goblin.y:
            if not goblin.flag_a:
                continue
            else:
                score1 += 10
                goblin.flag_a = False

    for goblin in goblins:
        u1 = goblin.hitbox[1] + goblin.hitbox[3]
        u2 = player1.hitbox[1] + player1.hitbox[3]
        if player1.hitbox[1] < u1 and u2 > goblin.hitbox[1]:
            u3 = player1.hitbox[0] + player1.hitbox[2]
            u4 = goblin.hitbox[0] + goblin.hitbox[2]
            if u3 > goblin.hitbox[0] and player1.hitbox[0] < u4:
                player1.hit()
                life_a = False
                timer = 30

    for obstacle in obstacles:
        if player1.y + player1.height < obstacle.y:
            if not obstacle.flag_a:
                continue
            else:
                score1 += 5
                obstacle.flag_a = False

    for obstacle in obstacles:
        o1 = obstacle.hitbox[1] + obstacle.hitbox[3]
        o2 = player1.hitbox[1] + player1.hitbox[3]
        if player1.hitbox[1] < o1 and o2 > obstacle.hitbox[1]:
            o3 = player1.hitbox[0] + player1.hitbox[2]
            o4 = obstacle.hitbox[0] + obstacle.hitbox[2]
            if o3 > obstacle.hitbox[0] and player1.hitbox[0] < o4:
                player1.hit()
                life_a = False
                timer = 30

    for goblin in goblins:
        if player2.y + player2.height > goblin.y:
            if not goblin.flag_b:
                continue
            else:
                score2 += 10
                goblin.flag_b = False

    for goblin in goblins:
        p1 = goblin.hitbox[1] + goblin.hitbox[3]
        p2 = player2.hitbox[1] + player2.hitbox[3]
        if player2.hitbox[1] < p1 and p2 > goblin.hitbox[1]:
            p3 = player2.hitbox[0] + player2.hitbox[2]
            p4 = goblin.hitbox[0] + goblin.hitbox[2]
            if p3 > goblin.hitbox[0] and player2.hitbox[0] < p4:
                player2.hit()
                life_b = False

    for obstacle in obstacles:
        if player2.y + player2.height > obstacle.y:
            if not obstacle.flag_b:
                continue
            else:
                score2 += 5
                obstacle.flag_b = False

    for obstacle in obstacles:
        m1 = obstacle.hitbox[1] + obstacle.hitbox[3]
        m2 = player2.hitbox[1] + player2.hitbox[3]
        if player2.hitbox[1] < m1 and m2 > obstacle.hitbox[1]:
            m3 = player2.hitbox[0] + player2.hitbox[2]
            m4 = obstacle.hitbox[0] + obstacle.hitbox[2]
            if m3 > obstacle.hitbox[0] and player2.hitbox[0] < m4:
                player2.hit()
                life_b = False

    if player1.y <= player2_initial[1] and count1 == 0:
        score1 += timer
        count1 += 1

    if player2.y >= player1_initial[1] and count2 == 0:
        score2 += timer
        count2 += 1

    if player1.y <= player2_initial[1]:
        timer = 30
        player1.visible = False
        player2.visible = True
        player1.x = player1_initial[0]
        player1.y = player1_initial[1] + 50
        level_a += 1
        l_inc_a += 1
        for goblin in goblins:
            goblin.flag_a = True
            if l_inc_a == 1 and l_inc_b == 1:
                goblin.vel *= level_a
        for obstacle in obstacles:
            obstacle.flag_a = True

    if player2.y >= player1_initial[1]:
        timer = 30
        player2.visible = False
        player1.visible = True
        player2.x = player2_initial[0]
        player2.y = player2_initial[1]
        level_b += 1
        l_inc_b += 1
        for goblin in goblins:
            goblin.flag_b = True
            goblin.vel *= level_b
        for obstacle in obstacles:
            obstacle.flag_b = True

    if timer <= 0:
        if player1.visible:
            life_a = False
            player1.visible = False
            player2.visible = True
            timer = 30
            player1.x = player1_initial[0]
            player1.y = player1_initial[1] + 50
            continue

    if timer <= 0:
        if player2.visible:
            life_b = False
            player2.visible = False
            player1.visible = True
            timer = 30
            player2.x = player2_initial[0]
            player2.y = player2_initial[1]
            continue

    if (not life_a and not life_b) or (not life_b):
        endscreen()
    else:
        redrawGameWindow()
pygame.quit()
