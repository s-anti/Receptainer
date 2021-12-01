import pygame, math, os
from colors import *



class Sprite:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.dx = 0
		self.dy = 0
		self.width = width
		self.height = height
		self.color = red
		self.friction = 0,9




class Character:
	def __init__(self, sprite):
		
		# TODO animación
		# images = []
		# for file_name in os.listdir(sprite):
		# 	image = pygame.image.load(sprite + os.sep + file_name).convert()
		# 	images.append(image)

		self.spriteder = pygame.image.load(sprite)
		self.spriteizq = pygame.transform.flip(self.spriteder, True, False)
		self.sprite = self.spriteder
		self.rect = self.sprite.get_rect()
		self.speed = 0
		self.acceleration = 3
		
		self.max_speed = 14
		

	def move(self, d):
		
		# TODO limite del techo y piso 

		if d != (0,0):
			if d.x > 0:
				self.sprite = self.spriteizq
			else: 
				self.sprite = self.spriteder

			d = d.normalize()
			self.speed += self.acceleration
			self.speed = min(self.speed, self.max_speed)
		
	
		#self.x += self.dx
		#self.y += self.dy
		#self.dy += Gravity

		self.rect = self.rect.move(
			self.speed*d.x,
			self.speed*d.y
			)
		
		
		
		
	#def jump(self):
		#self.speed*d.y


	

Gravity = 1

# Create game objects
#Character = Character (600, 0, 20, 40)
platforms = []
platforms.append(Sprite(600, 200, 400,20))
platforms.append(Sprite(600, 400, 600, 20))
platforms.append(Sprite(600, 600, 1000, 20))
platforms.append(Sprite(1000, 500, 100, 200))
platforms.append(Sprite(200, 500, 100, 200))



