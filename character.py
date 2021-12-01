import pygame, math
from colors import *

pygame.init()

# TODO: eliminar, uso exclusivo de prueba, manejar desde main o cÃ¡mara
width, height = 1500 , 800                          
screen = pygame.display.set_mode((width, height))   # LA PANTALLA
pygame.display.set_caption("Personaje")             # Titulo

clock = pygame.time.Clock()


class Character:
	def __init__(self, sprite):
		self.sprite = pygame.image.load(sprite)
		self.rect = self.sprite.get_rect()
		self.speed = 15

	def move(self, d):
		
		if d.xy != (0,0):
			d = d.normalize()


		self.rect = self.rect.move(
			self.speed*d.x,
			self.speed*d.y
			)

			
		screen.blit(self.sprite, self.rect)

	
char = Character("sprites/sprite_juan.png")

running = True
direccion = pygame.math.Vector2(0,0)



while running:

	screen.fill(white)

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

	
	pygame.display.update()
	clock.tick(45)

pygame.quit()