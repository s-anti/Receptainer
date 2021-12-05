import pygame, math

class Arma:
	def __init__(self, path, cadencia, t_recarga, cargador, dispersion, daño, tipo, bala_path =  "sprites/Arma/bala.png"):
		self.spriteizq = pygame.image.load(path)
		self.spriteder  = pygame.transform.flip(self.spriteizq, False, True)
		self.sprite = self.spriteder
		
		
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

	def update(self, pos, target):
		
		# Esta linea es secuestrada de google pero cambié dos numeros y anda joya, no la toquen
		angle = 180-math.atan2(target[1]-pos[1],target[0]-pos[0])*180/math.pi

		if angle > 90 and angle < 270:
			self.sprite = self.spriteder
		else: 
			self.sprite = self.spriteizq
			
		self.temp_sprite = pygame.transform.rotate(self.sprite, angle)
		self.temp_rect = self.temp_sprite.get_rect(center = pos)

		
		
	def shoot(self):
		#screen.blit(self.bala_sprite
		pass