import pygame, sys
from pygame import key
from pygame.locals import QUIT
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800,600))
files = ["Floor1.png", "Floor2.png", "Floor3.png", "Floor4.png"]
rooms = []
for j in range(4):
room = []
corner = j + 1
image = pygame.image.load(files[j])
image = pygame.transform.scale(image, (400,300))
while corner % 4 != 1:
if corner % 2 == 0:
image = pygame.transform.flip(image, False, True)
else:
image = pygame.transform.flip(image, True, False)
corner += 1

room.append(image)
room.append(pygame.transform.flip(image, True, False))
room.append(pygame.transform.flip(image, False, True))
room.append(pygame.transform.flip(image, True, True))
rooms.append(room)
index = 0

# image1 = pygame.image.load("Floor1.png")
# player = pygame.image.load("Isaac.png")
# player = pygame.transform.scale(player, (50,50))
# player_x = 0

# group = pygame.sprite.Group()
# class Player(pygame.sprite.Sprite):
# def __init__(self, x, y, width, height):
# pygame.sprite.Sprite.__init__(self, group)
# self.image = pygame.image.load("Isaac.png")
# self.image = pygame.transform.scale(self.image, (width, height))
# self.rect = pygame.Rect(x, y, width, height)
# def update(self):
# keys = pygame.key.get_pressed()
# if keys[pygame.K_RIGHT]:
# self.rect.x += 5
# player = Player(0, 0 , 25, 25)
clock = pygame.time.Clock()
t=0
while True:
clock.tick(60)
# keys = pygame.key.get_pressed()
# if keys[pygame.K_d]:
# player_x += 5
# mouse = pygame.mouse.get_pos()
# player_x = mouse[0]
events = pygame.event.get()
# for event in events:
# if event.type == pygame.KEYDOWN:
# if event.key == pygame.K_RIGHT:
# player_x += 100
# if event.type == pygame.QUIT:
pygame.quit()
sys.exit()
DISPLAYSURF.blit(rooms[index][0], (0, 0))
DISPLAYSURF.blit(rooms[index][1], (400, 0))
DISPLAYSURF.blit(rooms[index][2], (0, 300))
DISPLAYSURF.blit(rooms[index][3], (400, 300))

# DISPLAYSURF.blit(image1, (200,200))
# group.draw(DISPLAYSURF)
# group.update()
pygame.display.update()
t+=1
if t == 120:
# index= 0 if index==3 else index + 1
t=0