import pygame
import time

# Inicializar pygame
pygame.init()

# Crear una ventana
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pintar un píxel")

# Color del píxel (rojo en este caso)
red = (255, 0, 0)

# Posición del píxel
x, y = 100, 150


def rectangulo(x, y, k, color):
    for i in range(y,y+k):
        for j in range(x,x+k):
            screen.set_at((i,j), color)
            

# Bucle principal
running = True
k=0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pintar el fondo de negro
    screen.fill((50, 50, 50))

    # Pintar el píxel
    screen.set_at((x, y), red)
    #screen.set_at((x+1, y), red)
    #screen.set_at((x+2, y), red)
    #screen.set_at((x+3, y), red)
    rectangulo(10+k, 10+k, 300, red)
    k = k+10
    time.sleep(0.01)
    
    pygame.draw.rect(screen,red,(100,500,100,100))

    # Actualizar la pantalla
    pygame.display.flip()

# Salir de pygame
pygame.quit()


