import pygame
<<<<<<< HEAD
=======
import ChainChomp
import os
>>>>>>> parent of 3ae0b97... lanes


def drawMap(data, display):
    # map dimensions
    data.mapWidth = 7000
    data.mapHeight = 7000

    height = data.mapHeight
    width = data.mapWidth

    sx = data.scrollX
    sy = data.scrollY

    margin = 100
    baseRad = height * 1 // 5
    towerRad = height // 100

    tower1Color = (0, 0, 255)
    tower2Color = (255, 0, 0)

    # print(grassImage.get_height())

    # Draw the whole map
    # pygame.draw.rect(display, (0, 255, 0), (0 - data.scrollX, 0 - data.scrollY,
    # width, height))




    # Draws bases
    pygame.draw.ellipse(display, (153, 50, 204), (0 - baseRad - sx,
                                                  height - baseRad // 2 - sy,
                                                  baseRad * 2, baseRad))
    pygame.draw.ellipse(display, (153, 50, 204), (width - baseRad - sx,
                                                  0 - baseRad // 2 - sy,
                                                  baseRad * 2,
                                                  baseRad))

    # Draws blue towers
    pygame.draw.ellipse(display, tower1Color, (margin - towerRad - sx,
                                               height * 3 // 10 - towerRad // 2 - sy,
                                               towerRad * 2, towerRad))
    pygame.draw.ellipse(display, tower1Color, (margin - towerRad - sx,
                                               height // 2 - towerRad // 2 - sy,
                                               towerRad * 2, towerRad))
    pygame.draw.ellipse(display, tower1Color, (width // 2 - towerRad - sx,
                                               height - margin - towerRad // 2 - sy,
                                               towerRad * 2, towerRad))
    pygame.draw.ellipse(display, tower1Color, (width * 7 // 10 - towerRad - sx,
                                               height - margin - towerRad // 2 - sy,
                                               towerRad * 2, towerRad))
    pygame.draw.ellipse(display, tower1Color,
                        (width // 2 - 4 * margin - towerRad - sx,
                         height // 2 + 4 * margin - towerRad // 2 - sy,
                         towerRad * 2, towerRad))
    pygame.draw.ellipse(display, tower1Color, (width // 4 - towerRad - sx,
                                               height * 3 // 4 - towerRad // 2 - sy,
                                               towerRad * 2, towerRad))

    # Draws red towers
    pygame.draw.ellipse(display, tower2Color, (width * 3 // 10 - towerRad - sx,
                                               margin - towerRad // 2 - sy,
                                               towerRad * 2, towerRad))
    pygame.draw.ellipse(display, tower2Color, (width // 2 - towerRad - sx,
                                               margin - towerRad // 2 - sy,
                                               towerRad * 2, towerRad))
    pygame.draw.ellipse(display, tower2Color, (width - margin - towerRad - sx,
                                               height // 2 - towerRad // 2 - sy,
                                               towerRad * 2, towerRad))
    pygame.draw.ellipse(display, tower2Color, (width - margin - towerRad - sx,
                                               height * 7 // 10 - towerRad // 2 - sy,
                                               towerRad * 2, towerRad))
    pygame.draw.ellipse(display, tower2Color,
                        (width // 2 + 4 * margin - towerRad - sx,
                         height // 2 - 4 * margin - towerRad // 2 - sy,
                         towerRad * 2, towerRad))
    pygame.draw.ellipse(display, tower2Color, (width * 3 // 4 - towerRad - sx,
                                               height // 4 - towerRad // 2 - sy,
                                               towerRad * 2, towerRad))
<<<<<<< HEAD

=======
>>>>>>> parent of 3ae0b97... lanes

def move(data, x, y):
    # x, y is either 0 or 1 or -1
    data.scrollX += x * data.mapStep
    data.scrollY += y * data.mapStep


class backGround(pygame.sprite.Sprite):
<<<<<<< HEAD
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(
            'sprites/grass.png'
            ''), (1000, 1000))


def drawBoard(self, display):
    backGround.__init__(self)

    sx = self.scrollX
    sy = self.scrollY

    for i in range(7):
        for j in range(7):
            display.blit(self.image,
                         (0 - sx + 1000 * i, 0 - sy + 1000 * j, 1000, 1000))
=======
  def __init__(self):
      pygame.sprite.Sprite.__init__(self)
      self.road_h=pygame.image.load(os.path.join('sprites/grass_road_h.png'))
      self.road_h=pygame.transform.scale(self.road_h,(1000,1000))
      self.road_c3=pygame.image.load(os.path.join('sprites/grass_road_c3.png'))
      self.road_c3=pygame.transform.scale(self.road_c3,(1000,1000))
      self.road_c4=pygame.image.load(os.path.join('sprites/grass_road_c4.png'))
      self.road_c4=pygame.transform.scale(self.road_c4,(1000,1000))
      self.road_c1=pygame.image.load(os.path.join('sprites/grass_road_c1.png'))
      self.road_c1=pygame.transform.scale(self.road_c1,(1000,1000))
      self.road_c2=pygame.image.load(os.path.join('sprites/grass_road_c2.png'))
      self.road_c2=pygame.transform.scale(self.road_c2,(1000,1000))
      self.road_d=pygame.image.load(os.path.join('sprites/grass_road_d.png'))
      self.road_d=pygame.transform.scale(self.road_d,(1000,1000))
      self.road_du=pygame.image.load(os.path.join('sprites/grass_road_du.png'))
      self.road_du=pygame.transform.scale(self.road_du,(1000,1000))
      self.road_dd=pygame.image.load(os.path.join('sprites/grass_road_dd.png'))
      self.road_dd=pygame.transform.scale(self.road_dd,(1000,1000))
      self.road_vdl=pygame.image.load(os.path.join('sprites/grass_road_vdl.png'))
      self.road_vdl=pygame.transform.scale(self.road_vdl,(1000,1000))
      self.road_vdr=pygame.image.load(os.path.join('sprites/grass_road_vdr.png'))
      self.road_vdr=pygame.transform.scale(self.road_vdr,(1000,1000))
      self.road_hdd=pygame.image.load(os.path.join('sprites/grass_road_hdd.png'))
      self.road_hdd=pygame.transform.scale(self.road_hdd,(1000,1000))
      self.road_hdu=pygame.image.load(os.path.join('sprites/grass_road_hdu.png'))
      self.road_hdu=pygame.transform.scale(self.road_hdu,(1000,1000))
      self.road_v=pygame.image.load(os.path.join('sprites/grass_road_v.png'))
      self.road_v=pygame.transform.scale(self.road_v,(1000,1000))
      self.default=pygame.transform.scale(pygame.image.load(
          'sprites/grass.png'
          ''), (1000, 1000))
      self.image = self.default

def drawBoard(data, display):

  sx = data.scrollX
  sy = data.scrollY

  for i in range(7):
      for j in range(7):
          if(i==j and i==0):
            data.backGround.image=data.backGround.road_c3
          elif(i+j==6 and j==0):
            data.backGround.image=data.backGround.road_c2
          elif(i+j==6 and j==6):
            data.backGround.image=data.backGround.road_c1
          elif(i==j and i==6):
            data.backGround.image=data.backGround.road_c4
          elif(i+j==5 and j==0):
            data.backGround.image=data.backGround.road_hdu
          elif(i+j==7 and i==1):
            data.backGround.image=data.backGround.road_hdd
          elif(i+j==7 and j==1):
            data.backGround.image=data.backGround.road_vdr
          elif(i+j==5 and j==5):
            data.backGround.image=data.backGround.road_vdl
          elif(i+j==5):
            data.backGround.image=data.backGround.road_du
          elif(i+j==7):
            data.backGround.image=data.backGround.road_dd
          elif(i+j==6):
            data.backGround.image=data.backGround.road_d
          elif(j==0 or j==6):
            data.backGround.image=data.backGround.road_h
          elif(i==0 or i==6):
            data.backGround.image=data.backGround.road_v
          else:
            data.backGround.image = data.backGround.default
          display.blit(data.backGround.image,(0 - sx + 1000 * i, 0 - sy + 1000 * j, 1000, 1000))
>>>>>>> parent of 3ae0b97... lanes
