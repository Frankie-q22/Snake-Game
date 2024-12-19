
import pygame
from random import randrange

pygame.init()

#Creates Game Window
Screen_Width =  800
Screen_Height = 700
Tile_Size = 50
Range = (Tile_Size // 2 , Screen_Width - Tile_Size // 2 , Tile_Size)

# tuple for randomzing both x and y coordinates
Randomize_Position = lambda: [randrange(*Range), randrange(*Range)]

snake = pygame.rect.Rect([0, 0, Tile_Size -2, Tile_Size -2])
snake.center = Randomize_Position()
length = 1
segments = [snake.copy()]
snake_direction = (0,0)
Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
pygame.display.set_caption("Snake ~~~~:P   ")

clock = pygame.time.Clock()

while True:
 for event in pygame.event.get():
     if event.type == pygame.QUIT:
         exit()
     if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_w:
             snake_direction = (0,-Tile_Size)
         if event.key == pygame.K_a:
             snake_direction =(-Tile_Size,0)
         if event.key == pygame.K_s:
             snake_direction =(0,Tile_Size)
         if event.key == pygame.K_d:
             snake_direction =(Tile_Size,0)
 Screen.fill('Black')
 #function draws snake, and also makes appear in a different position everytime
 [pygame.draw.rect(Screen, 'green', segment) for segment in segments]
 #Allows snake to move
 snake.move_ip(snake_direction)
 segments.append(snake.copy())
 segments = segments[- length:]
 pygame.display.flip()
 clock.tick(60)   