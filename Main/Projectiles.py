import pygame
import math


class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, target, speed, damage):
        pygame.sprite.Sprite.__init__(self)
        self.pos = pos
        self.target = target
        self.dest = target.rect.center
        self.speed = speed
        self.image = pygame.Surface([5, 5])
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.image.fill((255, 0, 0))
        self.damage = damage

    def adjust(self, x, y, data):
        self.rect.x += x * data.mapStep
        self.rect.y += y * data.mapStep
    def move(self, data, epsilon=6):
        # location command
        destX, destY = self.dest[0], self.dest[1]

        # current location
        x, y = self.pos[0], self.pos[1]

        dx = destX - x
        dy = destY - y

        xDir, yDir = 1, 1

        if (dx < 0):
            xDir = -1
        if (dy < 0):
            yDir = -1

        if (dy < epsilon and dy > -epsilon and dx < epsilon and dx > -epsilon):
            self.movementState = 'still'
        elif (dy < epsilon and dy > -epsilon):
            x += self.speed * xDir
            if (xDir > 0):
                self.animationDirection = 'right'
            else:
                self.animationDirection = 'left'
        elif (dx < epsilon and dx > -epsilon):
            y += self.speed * yDir
            if (xDir > 0):
                self.animationDirection = 'right'
            else:
                self.animationDirection = 'left'

        else:
            theta = abs(math.atan(dy / dx))
            # calculate unit vector
            i = self.speed * math.cos(theta) * xDir
            j = self.speed * math.sin(theta) * yDir
            x += i
            y += j
            self.movementState = 'moving'
            if (abs(i) > abs(j) or yDir == 1):
                if (xDir > 0):
                    self.animationDirection = 'right'
                else:
                    self.animationDirection = 'left'
            else:
                self.animationDirection = 'up'

        self.rect.center = (x - data.scrollX, y - data.scrollY)
        self.pos = [x, y]
    def update(self, data):
        self.move(data)
        if (pygame.sprite.collide_rect(self, self.target)):
            print('target hit')
            self.target.health -= self.damage
            self.kill()


def initProjectiles(data):
    data.projectiles = pygame.sprite.Group()


def drawProjectiles(display, data):
    data.projectiles.update(data)
    data.projectiles.draw(display)
