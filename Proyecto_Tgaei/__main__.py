import pygame
from pygame.constants import FULLSCREEN, K_F11, KEYDOWN, RESIZABLE, VIDEOEXPOSE, VIDEORESIZE
from character import Character
from camera import Camera
from arma import Arma
from colors import *


pygame.init()

width, height = 1500 , 800                          
screen = pygame.display.set_mode((width, height),pygame.RESIZABLE)   # LA PANTALLA
pygame.display.set_caption("Tsteo")             # Titulo


char = Character("sprites/Juan_animado/sprite_3.png")
rifle1 = Arma(
	"sprites/Arma/Armas del zip del facu/Rifle de asalto1.png",
	5, 3, 30, 20, 10, "Shifle",
	)

escopeta_falopa = Arma(
	"sprites/Arma/Armas del zip del facu/sprite_0.png",
	3, 2, 1, 7, 9, "EZ_Copeta"
)

cam = Camera((width, height))

fondo = pygame.image.load("sprites/fondo.png")

running = True
direccion = pygame.math.Vector2(0,0)


clock = pygame.time.Clock()

while running:

	screen.fill(white)

	screen.blit(fondo, (350, 0))

	mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
	

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
	if event.type == KEYDOWN:
		if event.type == VIDEORESIZE:
			if not FULLSCREEN:
				screen = pygame.display.set_mode((event.w , event.h), pygame.RESIZABLE)
		
		if event.key == pygame.K_HOME:
			FULLSCREEN = not FULLSCREEN
			if FULLSCREEN:
				screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.FULLSCREEN)
			else:
				screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)

		#if event.type == pygame.mouse.get_pressed:
		if event.type == pygame.MOUSEBUTTONDOWN:
			rifle1.shoot()
	
	
	char.move_global(direccion)
	char.draw(0,screen)

	# TODO: encanutar esto en el arma y usar una sola fnución
	arma_vec = pygame.Vector2(rifle1.rect.centerx-mouse_pos.x, rifle1.rect.centery-mouse_pos.y)
	arma_rot = pygame.Vector2(arma_vec).angle_to(rifle1.rect.center) - 45 
	arma_shoot = pygame.mouse.get_pressed()[0]
	rifle1.update(arma_rot, char.rect.center)
	screen.blit(rifle1.temp_sprite, rifle1.temp_rect)
	# __

	cam.update((width/2, height/2), [char])
	
	pygame.display.update()
	clock.tick(45)


#if character die:
	#lives -=1 




pygame.quit()