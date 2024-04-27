import pygame, sys
import numpy as np

pygame.init()
clock = pygame.time.Clock()

X,Y = 1000,1000

screen = pygame.display.set_mode([X,Y])
pygame.display.set_caption("Rotating rod")

# Grid propeties
x = 0
y = Y
dist_grid = 25

# Ratio of mass of the rod and mass of the bullet
beta = 1

# Half of the length of the rod
R = 230

# Position of the center of mass of the system
x_cm = (R)/(beta+1)

# Initial angles of the to extremities
a1 = 0
a2 = np.pi

# Coordinates of the cm with respect to the top left
x0 = X//2 + x_cm
y0 = Y//2

# Distances of the extremes from the cm
l1 = R + x_cm
l2 = R - x_cm

# The two extremes and the cm
cm = pygame.math.Vector2(x0, y0)
p1 = pygame.math.Vector2(0,0)
p2 = pygame.math.Vector2(0,0)

d = R

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

    cos_norm = abs(np.cos(a1))/np.cos(a1)
    borderX = x0 + np.cos(a1)*(d+10)*cos_norm

    if np.sin(a1) >= 0:
        if pos.y <= y0 and pos.x <= borderX:
            y += v_cm

            a1 += va
            a2 += va

            pos.x = x0 - np.cos(a2)*(d-x_cm)
            pos.y = y0 + np.sin(a2)*(d-x_cm)

        else:
            pos.y -= vel

    if np.sin(a1) < 0:
        if pos.y > y0 and pos.x <= borderX:
            y += v_cm

            a1 += va
            a2 += va

            pos.x = x0 - np.cos(a2)*(d-x_cm)
            pos.y = y0 + np.sin(a2)*(d-x_cm)

        else:
            pos.y -= vel

    p1.x = cm.x - np.cos(a1)*l1
    p1.y = cm.y + np.sin(a1)*l1

    p2.x = cm.x - np.cos(a2)*l2
    p2.y = cm.y + np.sin(a2)*l2

    # Draw grid
    yax = pygame.font.SysFont("Comic Sans MS", 20)
    for i in range(200):
        pygame.draw.line(screen, (0,0,0), (x+dist_grid*i,0), (x+dist_grid*i,Y), 2)
        if y > dist_grid:
            write = yax.render(str(dist_grid*i), 1, (255,255,255))
            screen.blit(write, (X//2-10,y-dist_grid*i-Y//2))
            pygame.draw.line(screen, (0,0,0), (0,y-dist_grid*i), (X, y-dist_grid*i), 2)

    pygame.draw.line(screen, (255,0,0), (X//2,0), (X//2,Y), 2)
    pygame.draw.line(screen, (255,0,0), (0,y-Y//2), (X,y-Y//2), 2)

    # Rod
    pygame.draw.line(screen, (255,0,255), cm, p1, 8)
    pygame.draw.line(screen, (0,255,255), cm, p2, 8)

    # Bullet
    pygame.draw.circle(screen, (255,0,0), pos, 6)

    font = pygame.font.SysFont("Comic Sans MS", 35)
    write1 = font.render("Angular velocity: " + str(round(va*100,4)) + " rad/s", 1, (255,255,255))
    write2 = font.render("Velocity of the center of mass: " + str(round(v_cm,2)) + " m/s", 1, (255,255,255))

    screen.blit(write1, (10,10))
    screen.blit(write2, (10,30))

    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()

pygame.quit()
