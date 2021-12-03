import pygame


class Camera():
    # TODO: hacer que funcione bien correctamente 
    def __init__(self, size):
        self.position = pygame.Vector2(0,0)
        self.size = size

    def update(self, position, elemtents: list = []):
        self.position = position
#eloctaselacomecuadrada