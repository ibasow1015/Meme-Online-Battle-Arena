import pygame
#hello

class Main(object):
	def init(self):
		pass

	def mousePressed(self, x, y):
		print(x, y)

	def mouseReleased(self, x, y):
		pass

	def mouseMotion(self, x, y):
		pass

	def mouseDrag(self, x, y):
		pass

	def keyPressed(self, keyCode, modifier):
		pass

	def keyReleased(self, keyCode, modifier):
		pass

	def timerFired(self, dt):
		pass

	def redrawAll(self, screen):
		pass

	def isKeyPressed(self, key):
		return self._keys.get(key, False)

	def __init__(self, width=600, height=600, fps=50, title='Settlers of '
	                                                        'Catan'):
		self.width = width
		self.height = height
		self.fps = fps
		self.title = title
		self.bgColor = (255, 255, 255)
		pygame.init()

	def run(self):
		clock = pygame.time.Clock()
		screen = pygame.display.set_mode((self.width, self.height))

		pygame.display.set_caption(self.title)

		self._keys = dict()

		self.init()
		playing = True
		while playing:
			time = clock.tick(self.fps)
			self.timerFired(time)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					self.mousePressed(*(event.pos))
				elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
					self.mouseReleased(*(event.pos))
				elif event.type == pygame.MOUSEMOTION and event.buttons == (
						0,0,0):
					self.mouseMotion(*(event.pos))
				elif event.type == pygame.MOUSEMOTION and event.buttons[0] == 1:
					self.mouseDrag(*(event.pos))
				elif event.type == pygame.KEYDOWN:
					self._keys[event.key] = True
					self.keyPressed(event.key, event.mod)
				elif event.type == pygame.KEYUP:
					self._keys[event.key] = False
					self.keyReleased(event.key, event.mod)
				elif event.type == pygame.QUIT:
					playing = False

			screen.fill(self.bgColor)
			self.redrawAll(screen)
			pygame.display.flip()

		pygame.quit()

def main():
	game = Main()
	game.run()

if __name__ == '__main__':
	main()