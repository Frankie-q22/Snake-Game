
import pygame
from random import randrange

pygame.init()

#Creates Game Window
Screen_Width =  800
Screen_Height = 700
Tile_Size = 50
Range_X = (Tile_Size, Screen_Width - Tile_Size, Tile_Size)
Range_Y = (Tile_Size, Screen_Height - Tile_Size, Tile_Size)
# tuple for randomzing both x and y coordinates
Randomize_Position = lambda: [randrange(*Range_X), randrange(*Range_Y)]

snake = pygame.rect.Rect([0, 0, Tile_Size -2, Tile_Size -2])
length = 1
segments = [snake.copy()]
snake_direction = (0,0)
apple = pygame.rect.Rect([0, 0, Tile_Size -2, Tile_Size -2])
apple.center = Randomize_Position()
#add score
#score = 0
#score + 1
time, time_step = 0, 110
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
 #borders and eating yourself
 #cant_eat_yourself = pygame.Rect.collidelist(snake, segments[:-1]) != -1
 if snake.left < 0 or snake.right > 800 or snake.top < 0 or snake.bottom > 700: #or #cant_eat_yourself:
     snake.center, apple.center = Randomize_Position(), Randomize_Position()
     length, snake_direction = 1, (0,0)
     segments = [snake.copy()]
 #check to see if apple was eaten
 if snake.center == apple.center:
     apple.center = Randomize_Position()
     length += 1
 #draw apple
 pygame.draw.rect(Screen, 'red', apple)
 #function draws snake, and also makes appear in a different position everytime
 [pygame.draw.rect(Screen, 'green', segment) for segment in segments]
 #Allows snake to move
 current_timing = pygame.time.get_ticks()
 if current_timing - time > time_step:
     time = current_timing
     snake.move_ip(snake_direction)
     segments.append(snake.copy())
     segments = segments[- length:]
 pygame.display.flip()
 clock.tick(60)   