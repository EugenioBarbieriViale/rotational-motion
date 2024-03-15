import pygame, sys
import numpy as np

pygame.init()
clock = pygame.time.Clock()

X,Y = 1000,1000

screen = pygame.display.set_mode([X,Y])
pygame.display.set_caption("Angular momentum")


def grid(n, x, ys, X, Y, vel):
    dist = X/n

    for i in range(n):
        for j in range(n):
            ys[j] += vel

        # Vertical lines
        x += dist
        pygame.draw.line(screen, (0,0,0), (x,0), (x,Y), 2)

        # Horizontal lines
        pygame.draw.line(screen, (0,0,0), (0,ys[i]), (X,ys[i]), 2)

n = 20
ys = [(X/n)*k for k in range(n)]

# Ratio of mass of the rod and mass of the bullet
beta = 5

# Half of the length of the rod
R = 300

# Position of the center of mass of the system
x_cm = (R)/(beta+1)

# Initial angles of the to extremities
a1 = 0
a2 = np.pi

# Coordinates of the cm with respect to the top left
x0 = X//2 + x_cm
y0 = Y//2 + 200

# Distances of the extremes from the cm
l1 = R + x_cm
l2 = R - x_cm

# The two extremes and the cm
cm = pygame.math.Vector2(x0, y0)
p1 = pygame.math.Vector2(0,0)
p2 = pygame.math.Vector2(0,0)

dist_input = 250 # from the middle of the rod
d = dist_input - x_cm

# Initial position and velocity of the bullet
pos = pygame.math.Vector2(X//2 + d-6, y0 + 200)
vel = 2

v_cm = (vel)/(beta+1) # velocity of the center of mass
va = 6*vel/(2*R*(beta+4)) # angular velocity


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((200,200,200))

    # if pos.y <= y0 + np.sin(a1)*d and pos.x > x0 - np.cos(a1)*d-10:
    # if pos.y <= y0 + np.sin(a1)*d:
    if a2 < 6.3:
        if pos.y <= y0: 

            a1 += va
            a2 += va

            pos.x = x0 - np.cos(a2)*(d-x_cm)
            pos.y = y0 + np.sin(a2)*(d-x_cm)

            y0 -= v_cm
            cm.y -= v_cm

        else:
            pos.y -= vel

    if a2 > 6.3:
        if pos.y >= y0: 

            a1 += va
            a2 += va

            pos.x = x0 - np.cos(a2)*(d-x_cm)
            pos.y = y0 + np.sin(a2)*(d-x_cm)

            y0 -= v_cm
            cm.y -= v_cm

        else:
            pos.y -= vel

    p1.x = cm.x - np.cos(a1)*l1
    p1.y = cm.y + np.sin(a1)*l1

    p2.x = cm.x - np.cos(a2)*l2
    p2.y = cm.y + np.sin(a2)*l2

    # Draw grid
    grid(n, 0, ys, X, Y, 0)

    # Rod
    pygame.draw.line(screen, (255,0,255), cm, p1, 8)
    pygame.draw.line(screen, (0,255,255), cm, p2, 8)

    # Projectile
    pygame.draw.circle(screen, (255,0,0), pos, 6)

    font = pygame.font.SysFont("Comic Sans MS", 35)
    write1 = font.render("Angular velocity: " + str(round(va*100,4)) + " rad/s", 1, (255,255,255))
    write2 = font.render("Velocity of the center of mass: " + str(round(v_cm*10,2)) + " m/s", 1, (255,255,255))

    screen.blit(write1, (10,10))
    screen.blit(write2, (10,30))

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

pygame.quit()
