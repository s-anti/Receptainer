import pygame

run = True

pygame.init()
screen = pygame.display.set_mode((1600, 900))

clock = pygame.time.Clock()

foto = pygame.image.load("sprites/Ciudad choreaida/Sample.png")

x = y = 0

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: run = False

	screen.fill((40,10,10))

	screen.blit(foto, (x,y))


	clock.tick(75)
	pygame.display.update()