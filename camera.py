import pygame

class camera():
    def __init__(self, target):
        self.x = target.x
        self.y = target.y

    def update(self,target):
        self.x = target.x
        self.y = target.y
#eloctaselacomecuadrada