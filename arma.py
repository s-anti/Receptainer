import pygame, math

class Arma:
	def __init__(
			self,
			path: str = "",			cadencia: float = 200,
			t_recarga: float = 4.5,	cargador: int = 15,
			dispersion: int = 20,	daño: float = 10,
			tipo: str = "",			velocidad_tiro: int = 15,
			bala_path: str = "sprites/Arma/bala.png"
		):
		
		self.spriteizq = pygame.image.load(path)
		self.spriteder  = pygame.transform.flip(self.spriteizq, False, True)
		self.sprite = self.spriteder
		self.rect = self.sprite.get_rect()
		self.angle = 0

		self.bala_sprite = pygame.image.load(bala_path)

		self.rate = cadencia
		self.t_recarga = t_recarga
		self.cargador = cargador
		self.dispersion = dispersion
		self.daño = daño
		self.v_tiro = velocidad_tiro


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
			
		self.sprite = pygame.transform.rotate(self.sprite, angle)
		self.rect = self.sprite.get_rect(center = pos)
		self.angle = angle
		
		
	def shoot(self, angle):
		
		sprite = pygame.transform.rotate(self.bala_sprite, angle)
		
		w = self.spriteder.get_width()/2
		posx = self.rect.centerx - w * math.cos(math.radians(angle))
		posy = self.rect.centery + w * math.sin(math.radians(angle))
		
		rect = sprite.get_rect(center = (posx, posy))
		
		return {"sprite": sprite, "rect": rect, "angle": angle, "birth": 0}


	def update_bullets(self, bullets, time):
		
		for bullet in bullets:
			bullet["rect"].x -= self.v_tiro * math.cos(math.radians(bullet["angle"]))
			bullet["rect"].y += self.v_tiro * math.sin(math.radians(bullet["angle"]))


			
			# La saco de la lista de actualización para el frame
			# que viene por que si no había un jitter feo
			if time - bullet["birth"] > 8000: #timepo de vida de la bala:
				bullets.remove(bullet)
			
		return bullets
	
	def draw(self, screen, cam_pos):
		screen.blit(self.sprite, self.rect)
	
	def draw_bullets(self, screen, cam_pos, bullets):
		for i in bullets: screen.blit(i["sprite"], i["rect"])