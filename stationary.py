import pygame, sys
import numpy as np

pygame.init()
clock = pygame.time.Clock()

X,Y = 1000,800

screen = pygame.display.set_mode([X,Y])
pygame.display.set_caption("Angular momentum")

# ---------------- ROD
M = 5
R = 200
p1 = pygame.math.Vector2(X//2, Y//2)
p2 = pygame.math.Vector2(X//2, Y//2)

a1 = 0
a2 = np.pi

# Sense of rotation: clockwise -1; counterclockwise 1
S = 1
va = 0

# --------------- BALL
m = 2
d = 182
pos = pygame.math.Vector2(X//2 + d-6, Y//2 - 250)
vel = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    if pos.y >= Y//2 + np.sin(a1)*d and pos.x >= X//2 + np.cos(a1)*d*S-10:
        va = (d*m*vel)/(1/3*M*R*R + m*d*d)
        a1 += va
        a2 += va

        pos.x = X//2 + np.cos(a1)*d*S
        pos.y = Y//2 + np.sin(a1)*d

    else:
        pos.y += vel

    p1.x = X//2 + np.cos(a1)*R*S
    p1.y = Y//2 + np.sin(a1)*R

    p2.x = X//2 + np.cos(a2)*R*S
    p2.y = Y//2 + np.sin(a2)*R

    # pygame.draw.circle(screen, (255,0,0), p1, 7)
    # pygame.draw.circle(screen, (0,255,0), p2, 7)

    pygame.draw.line(screen, (255,255,255), p1, p2, 8)
    pygame.draw.circle(screen, (0,0,255), (X//2,Y//2), 5)

    pygame.draw.circle(screen, (255,0,0), pos, 6)


    font = pygame.font.SysFont("Comic Sans MS", 30)
    l1 = font.render("Angular velocity: " + str(round(va*100,3)) + " rad/s", 1, (255,255,255))
    l2 = font.render("Distance from rotation axis: " + str(d) + " cm", 1, (255,255,255))

    screen.blit(l1, (10,10))
    screen.blit(l2, (10,30))

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

pygame.quit()
