import pygame
from character import Character
from colors import *

pygame.init()

char = Character("sprites/sprite_juan.png")

fondo = pygame.image.load("sprites/fondo.png")

running = True
direccion = pygame.math.Vector2(0,0)

# TODO: eliminar, uso exclusivo de prueba, manejar desde main o cÃ¡mara
width, height = 1500 , 800                          
screen = pygame.display.set_mode((width, height))   # LA PANTALLA
pygame.display.set_caption("Personaje")             # Titulo

clock = pygame.time.Clock()

while running:

	screen.fill(white)

	screen.blit(fondo, (350, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT: running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				direccion.x = -1
			if event.key == pygame.K_d:
				direccion.x = 1
			if event.key == pygame.K_w:
				direccion.y = -1
			if event.key == pygame.K_s:
				direccion.y = 1
			
			

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a and direccion.x == -1:
				direccion.x = 0
			if event.key == pygame.K_d and direccion.x == 1:
				direccion.x = 0
			if event.key == pygame.K_w and direccion.y == -1:
				direccion.y = 0
			if event.key == pygame.K_s and direccion.y == 1:
				direccion.y = 0

	char.move(direccion)

	screen.blit(char.sprite, char.rect)
	
	pygame.display.update()
	clock.tick(45)


#if character die:
	#lives -=1 




pygame.quit()