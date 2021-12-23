import pygame, sys
from random import randrange
from agent import Agent
from image import Image

# general setup
pygame.init()
clock = pygame.time.Clock()

# create display screen
screen_width = 1440
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

# background map image
background = pygame.transform.smoothscale(pygame.image.load("img/map.svg"), (screen_width, screen_height))

# create image instance to prosses images
image = Image()

# list of colored pixels coords
colored_pixel_coords = []
colored_pixel_coords = image.select_colored_pixel_coords(background)

# agent sprite group
agent_group = pygame.sprite.Group()

# agent list
agent_list = []

# groupping and listing agents
for i in range(100):
    starting_pos = image.select_random_colored_pixel_coords(colored_pixel_coords)
    ending_pos = image.select_random_colored_pixel_coords(colored_pixel_coords)
    agent = Agent(starting_pos, ending_pos)

    agent_group.add(agent)
    agent_list.append(agent)

# main loop
while True:
    # check exit status
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # refresh screen every frame
    pygame.display.flip()
    clock.tick(20)
    screen.blit(background, (0, 0))

    # draw agents
    agent_group.update()
    agent_group.draw(screen)
    
