import pygame
import os


class GoldIcon(pygame.sprite.Sprite):
    def __init__(self, data, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('sprites/gold_icon.png'))
        self.image = pygame.transform.scale(self.image, (
        int(data.width * .03), int(data.width * .03)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class ArmorIcon(pygame.sprite.Sprite):
    def __init__(self, data, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('sprites/armor_icon.png'))
        self.image = pygame.transform.scale(self.image, (
        int(data.width * .02), int(data.width * .02)))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class SpeedIcon(pygame.sprite.Sprite):
    def __init__(self, data, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('sprites/speed_icon.png'))
        self.image = pygame.transform.scale(self.image, (
        int(data.width * .02), int(data.width * .02)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class RegenIcon(pygame.sprite.Sprite):
    def __init__(self, data, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('sprites/regen_icon.png'))
        self.image = pygame.transform.scale(self.image, (
        int(data.width * .02), int(data.width * .02)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class ResistIcon(pygame.sprite.Sprite):
    def __init__(self, data, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('sprites/resist_icon.png'))
        self.image = pygame.transform.scale(self.image, (
        int(data.width * .02), int(data.width * .02)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class MagicIcon(pygame.sprite.Sprite):
    def __init__(self, data, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((data.width * .02, data.width * .02))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class DamageIcon(pygame.sprite.Sprite):
    def __init__(self, data, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((data.width * .02, data.width * .02))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


def initIcons(data):
    data.icons = pygame.sprite.Group()
    goldIconX = data.width * .625
    goldIconY = data.height - data.width * .0225
    data.icons.add(GoldIcon(data, goldIconX, goldIconY))
    armorIconX = data.width * .2
    armorIconY = data.height - data.width * .11
    data.icons.add(ArmorIcon(data, armorIconX, armorIconY))
    speedIconX = data.width * .25
    speedIconY = data.height - data.width * .11
    data.icons.add(SpeedIcon(data, speedIconX, speedIconY))
    regenIconX = data.width * .2
    regenIconY = data.height - data.width * .07
    data.icons.add(RegenIcon(data, regenIconX, regenIconY))
    resistIconX = data.width * .25
    resistIconY = data.height - data.width * .07
    data.icons.add(ResistIcon(data, resistIconX, resistIconY))
    magicIconX = data.width * .2
    magicIconY = data.height - data.width * .03
    data.icons.add(MagicIcon(data, magicIconX, magicIconY))
    damageIconX = data.width * .25
    damageIconY = data.height - data.width * .03
    data.icons.add(DamageIcon(data, damageIconX, damageIconY))


def drawIcons(display, data):
    data.icons.draw(display)
