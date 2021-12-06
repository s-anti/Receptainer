import pygame, random
from character import Character
#from camera import Camera
from arma import Arma
from colors import *


pygame.init()

width, height = 1500 , 800                          
screen = pygame.display.set_mode((width, height))   # LA PANTALLA
pygame.display.set_caption("Tsteo")             # Titulo

fondo = pygame.image.load("sprites/fondo.png")

char = Character("sprites/Juan_animado/sprite_3.png")
player_shooting = False
player_can_shoot = True

rifle1 = Arma(
	"sprites/Arma/Armas del zip del facu/Rifle de asalto1.png",
	cadencia = 50, dispersion= 5
)

escopeta_falopa = Arma(
	"sprites/Arma/Armas del zip del facu/sprite_0.png",
	3, 2, 1, 7, 9, "EZ_Copeta"
)

#cam = Camera((width, height))


running = True
direccion = pygame.math.Vector2(0,0)

bullets = []


dibujables = [fondo, char, rifle1]


clock = pygame.time.Clock()

while running:

	time = pygame.time.get_ticks()

	screen.fill(white)

	

	mouse_pos = pygame.mouse.get_pos()
	
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

		#if event.type == pygame.mouse.get_pressed:
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0] == True:
				player_shooting = True
			#elif pygame.mouse.get_pressed()[2] == True:
				#[2] es el derecho, el [1] es la rueda
		if event.type == pygame.MOUSEBUTTONUP:
			if pygame.mouse.get_pressed()[0] == False:
				player_shooting = False

		if event.type == pygame.USEREVENT:
			player_can_shoot = True
	
	
	char.move_global(direccion)
	#screen.blit(char.sprite, char.rect)

	rifle1.update(char.rect.center, mouse_pos)
	#screen.blit(rifle1.sprite, rifle1.rect)
	
	if player_shooting:
		
		if player_can_shoot:
			angle = random.uniform(
				rifle1.angle - rifle1.dispersion,
				rifle1.angle + rifle1.dispersion)
			b = rifle1.shoot(angle)
			b["birth"] = time
			bullets.append(b)
			player_can_shoot = False
			pygame.time.set_timer(pygame.USEREVENT, rifle1.rate, 1)
		

	bullets = rifle1.update_bullets(bullets, time)

	#if not bullets in dibujables: dibujables.append(bullets)

	#for i in bullets: screen.blit(i["sprite"], i["rect"])

	#cam.update(char.rect.center, screen, dibujables)
	
	char.draw(screen, 0)
	rifle1.draw(screen, 0)
	rifle1.draw_bullets(screen, 0, bullets)

	pygame.display.update()
	clock.tick(45)


#if character die:
	#lives -=1 




pygame.quit()