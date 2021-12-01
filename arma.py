import pygame

class Arma:
	def __init__(self, path):
		self.image = pygame.image.load(path)
		self.direction = 0 # RADIANES