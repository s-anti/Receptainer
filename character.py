import pygame

pygame.init()

# TODO: eliminar, uso exclusivo de prueba, manejar desde main o cámara
width, height = 1600, 900                          
screen = pygame.display.set_mode((width, height))   # LA PANTALLA
pygame.display.set_caption("Personaje")             # Titulo



WHITHE =(255,255,255)	# TODO: mover a archivo colores
BLACK = (0,0,0) 		# TODO: mover a archivo colores


running = True
while running:
	screen.fill(BLACK)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

pygame.quit()
