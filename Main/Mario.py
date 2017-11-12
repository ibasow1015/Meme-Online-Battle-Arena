import Characters
import pygame
import os


class Mario(Characters.Player):
    def __init__(self, data, pos, name):
        Characters.Player.__init__(self, data, pos, name)
        self.width = 25
        self.height = 50
        self.image = pygame.image.load(
            os.path.join('sprites/mario/mario_r1.png'))
        self.image = pygame.transform.scale(self.image,
                                            (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.width = 25
        self.height = 50

        self.character = 'Mario'

        self.regen = 10

        self.health = 600
        self.maxHealth = 600
        self.energy = 600
        self.maxEnergy = 600
        self.speed = 10
        self.armor = 0
        self.regen = 0
        self.damage = 0
        self.magic = 0
        self.resist = 0

        self.ability4Active = False
        self.ability4Time = 0
        self.ability4Timer = 300

        self.ability3Active = False
        self.ability3Time = 0
        self.ability3Timer = 100

    def abilityTimers(self):
        if (self.ability4Active):
            self.ability4Time += 1
            if (self.ability4Time >= self.ability4Timer):
                self.ability4Active = False
                self.ability4Time = 0
                self.armor -= 20
                self.maxHealth -= 600
                self.width -= 75
                self.height -= 150
                if (self.health > self.maxHealth):
                    self.health = self.maxHealth
        if (self.ability3Active):
            self.ability3Time += 1
            if (self.ability3Time >= self.ability3Timer):
                self.ability3Active = False
                self.ability3Time = 0
                self.armor -= 10
                self.health -= 10
                self.width -= 25
                self.height -= 50


    def ability1(self):
        self.health -= 50
        if (self.health < 0):
            self.health = 0
        self.energy += 50
        if (self.energy > self.maxEnergy):
            self.energy = self.maxEnergy


    def ability2(self):
        if (self.energy > 50):
            self.health += 50
            if (self.health > self.maxHealth):
                self.health = self.maxHealth
            self.energy -= 50
            if (self.energy < 0):
                self.energy = 0


    def ability3(self):
        if (self.energy > 100 and self.ability3Active == False):
            self.energy -= 100
            self.ability3Active = True
            self.armor += 10
            self.health += 10
            self.width += 25
            self.height += 50


    def ability4(self):
        if (self.energy > 200 and self.ability4Active == False):
            self.energy -= 200
            self.ability4Active = True
            self.armor += 20
            self.maxHealth += 600
            self.health += 600
            self.width += 75
            self.height += 150


    def getCenter(self):
        return self.rect.center


    def animateWalk(self, direction):
        self.animationState += 1
        self.animationState %= 4
        if (direction == 'right'):
            if (self.movementState == 'still'):
                self.image = pygame.image.load(
                    os.path.join('sprites/mario/mario_r1.png'))
                self.image = pygame.transform.scale(self.image,
                                                    (self.width, self.height))
            else:
                if (self.animationState == 0):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario/mario_r1.png'))
                    self.image = pygame.transform.scale(self.image,
                                                        (self.width, self.height))
                elif (self.animationState == 1):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario/mario_r2.png'))
                    self.image = pygame.transform.scale(self.image,
                                                        (self.width, self.height))
                elif (self.animationState == 2):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario/mario_r3.png'))
                    self.image = pygame.transform.scale(self.image,
                                                        (self.width, self.height))
                elif (self.animationState == 3):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario/mario_r4.png'))
                    self.image = pygame.transform.scale(self.image,
                                                        (self.width, self.height))
        if (direction == 'left'):
            if (self.movementState == 'still'):
                self.image = pygame.image.load(
                    os.path.join('sprites/mario/mario_l1.png'))
                self.image = pygame.transform.scale(self.image,
                                                    (self.width, self.height))
            else:
                if (self.animationState == 0):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario/mario_l1.png'))
                    self.image = pygame.transform.scale(self.image,
                                                        (self.width, self.height))
                elif (self.animationState == 1):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario/mario_l2.png'))
                    self.image = pygame.transform.scale(self.image,
                                                        (self.width, self.height))
                elif (self.animationState == 2):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario/mario_l3.png'))
                    self.image = pygame.transform.scale(self.image,
                                                        (self.width, self.height))
                elif (self.animationState == 3):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario/mario_l4.png'))
                    self.image = pygame.transform.scale(self.image,
                                                        (self.width, self.height))
        if (direction == 'up'):
            if (self.movementState == 'still'):
                self.image = pygame.image.load(
                    os.path.join('sprites/mario/mario_uN.png'))
                self.image = pygame.transform.scale(self.image,
                                                    (self.width, self.height))
            else:
                if (self.animationState == 0 or self.animationState == 2):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario/mario_u1.png'))
                    self.image = pygame.transform.scale(self.image,
                                                        (self.width, self.height))
                elif (self.animationState == 1 or self.animationState == 3):
                    self.image = pygame.image.load(
                        os.path.join('sprites/mario/mario_u2.png'))
                    self.image = pygame.transform.scale(self.image,
                                                        (self.width, self.height))

