import pygame
import drawMap


def drawTaskbar(display, data):
    #drawMinimap(display, data)
    drawStats(display, data)
    drawItemSlots(display, data)
    drawAbilitySlots(display, data)
    drawResourceBars(display, data)


def drawItemSlots(display, data):
    boxX = data.width * .6
    boxY = data.height - data.width * .13
    boxWidth = data.width * .17
    boxHeight = data.width * .13
    pygame.draw.rect(display, (0, 0, 0), (boxX, boxY, boxWidth, boxHeight))
    slotWidth = data.width * .03
    slotMargin = data.width * .01
    for x in range(3):
        for y in range(2):
            pygame.draw.rect(display, (255, 255, 255), (
            boxX + slotMargin + (slotMargin + slotWidth) * x,
            boxY + slotMargin + (slotMargin + slotWidth) * y, slotWidth,
            slotWidth))
    pygame.draw.rect(display, (255, 255, 255), (
    (boxX + slotMargin + (slotMargin + slotWidth) * 3),
    boxY + slotMargin + (slotWidth + slotMargin) * .5, slotWidth, slotWidth))
    goldLabel = data.font.render(str(data.player.gold), 1, (255, 255, 255))
    display.blit(goldLabel, (data.width * .65, data.height - data.width * .04))


def drawStats(display, data):
    boxX = data.width * .18
    boxY = data.height - data.width * .13
    boxWidth = data.width * .12
    boxHeight = data.width * .13
    pygame.draw.rect(display, (0, 0, 0), (boxX, boxY, boxWidth, boxHeight))
    armorLabel = data.font.render(str(data.player.armor), 1, (255, 255, 255))
    display.blit(armorLabel,
                 (data.width * .215, data.height - data.width * .125))
    speedLabel = data.font.render(str(data.player.speed), 1, (255, 255, 255))
    display.blit(speedLabel,
                 (data.width * .265, data.height - data.width * .125))
    regenLabel = data.font.render(str(data.player.regen), 1, (255, 255, 255))
    display.blit(regenLabel,
                 (data.width * .215, data.height - data.width * .085))
    resistLabel = data.font.render(str(data.player.resist), 1, (255, 255, 255))
    display.blit(resistLabel,
                 (data.width * .265, data.height - data.width * .085))
    magicLabel = data.font.render(str(data.player.magic), 1, (255, 255, 255))
    display.blit(magicLabel,
                 (data.width * .215, data.height - data.width * .045))
    damageLabel = data.font.render(str(data.player.damage), 1, (255, 255, 255))
    display.blit(damageLabel,
                 (data.width * .265, data.height - data.width * .045))


def drawAbilitySlots(display, data):
    boxX = data.width * .3
    boxY = data.height - data.width * .13
    boxWidth = data.width * .3
    boxHeight = data.height * .085
    pygame.draw.rect(display, (0, 0, 0), (boxX, boxY, boxWidth, boxHeight))
    slotMargin = data.width * .0125
    slotWidth = data.width * .06
    for i in range(4):
        pygame.draw.rect(display, (0, 0, 255), (
        boxX + slotMargin + (slotMargin + slotWidth) * i, boxY + slotMargin,
        slotWidth, slotWidth))


def drawResourceBars(display, data):
    boxX = data.width * .3
    HealthboxY = data.height - data.width * .05
    EnergyboxY = data.height - data.width * .025
    boxWidth = data.width * .3
    boxHeight = data.height * .025
    pygame.draw.rect(display, (255, 0, 0),
                     (boxX, HealthboxY, boxWidth, boxHeight))
    healthPercentage = data.player.health / data.player.maxHealth
    pygame.draw.rect(display, (0, 255, 0),
                     (boxX, HealthboxY, boxWidth * healthPercentage, boxHeight))
    pygame.draw.rect(display, (255, 0, 0),
                     (boxX, EnergyboxY, boxWidth, boxHeight))
    energyPercentage = data.player.energy / data.player.maxEnergy
    pygame.draw.rect(display, (255, 255, 0),
                     (boxX, EnergyboxY, boxWidth * energyPercentage, boxHeight))

def drawMinimap(display, data):
    print(data.minimap.width)
    data.minimap.drawMap(display)

