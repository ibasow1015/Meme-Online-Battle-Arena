import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self,name):
		pygame.sprite.Sprite.__init__(self)

		self.image=pygame.Surface(50,50)
		self.rect=self.image.get_rect()