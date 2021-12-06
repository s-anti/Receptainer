import pygame


class Camera():
    # TODO: hacer que funcione bien correctamente 
    def __init__(self, size):
        self.position = pygame.Vector2(0,0)
        self.size = size

    def update(self, position, screen, elements: list = []):
        self.position = position

        for element in elements:
            if isinstance(element, pygame.Surface):
                screen.blit(element, (0,0))
            
            elif isinstance(element, list):
                for bullet in element: screen.blit(bullet["sprite"], bullet["rect"])
        else:


#eloctaselacomecuadrada