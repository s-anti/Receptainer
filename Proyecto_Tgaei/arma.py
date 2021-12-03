import pygame

class Arma:
	def __init__(self, path, cadencia, t_recarga, cargador, dispersion, daño, tipo, bala_path =  "sprites/Arma/bala.png"):
		self.spriteder = pygame.image.load(path)
		self.spriteizq  = pygame.transform.flip(self.spriteder, False, True)
		self.rect = self.spriteder.get_rect()
		
		self.bala_sprite = pygame.image.load(bala_path)

		self.rate = cadencia
		self.t_recarga = t_recarga
		self.cargador = cargador
		self.dispersion = dispersion
		self.daño = daño

		#if tipo == "Escopeta":
			#cadencia == 0.75
			#t_recarga == 0.9
			#cargador == 
			
			
			# TODO: Hacer que sea una escopeta
			#pass

	def update(self, rotation, position):
	
		if abs(rotation) > 90:
			sprite = self.spriteizq
			
		else:
			sprite = self.spriteder
			
		
		self.temp_sprite = pygame.transform.rotate(sprite, rotation)
		self.temp_rect = self.temp_sprite.get_rect(center = sprite.get_rect(center = (position)).center)

		self.rect.center = position

		self.temp_rect.centerx = position[0]
		self.temp_rect.centery = position[1] + sprite.get_size()[1]/2
		
	def shoot(self):
		#screen.blit(self.bala_sprite
		pass