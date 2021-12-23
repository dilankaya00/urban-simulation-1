import pygame
from random import randrange
from image import Image
from time import sleep

# create agent class inheritiance from pygame sprite class
class Agent(pygame.sprite.Sprite):

    def __init__(self, starting_pos, ending_pos):
        super().__init__()
        
        self.starting_pos = starting_pos
        self.starting_pos_x = starting_pos[0]
        self.starting_pos_y = starting_pos[1]

        self.ending_pos = ending_pos
        self.ending_pos_x = ending_pos[0]
        self.ending_pos_y = ending_pos[1]

        self.image = pygame.image.load("img/man.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = [self.starting_pos_x, self.starting_pos_y]

        img = Image()
        self.nearest_road_coords, self.min_distance_index = img.find_nearest_road_coords(self.starting_pos)

        self.right_flag = False
        self.left_flag = False
        self.top_flag = False
        self.bottom_flag = False

        if self.min_distance_index == 0:
            self.right_flag = True
        elif self.min_distance_index == 1:
            self.left_flag = True
        elif self.min_distance_index == 2:
            self.top_flag = True
        elif self.min_distance_index == 3:
            self.bottom_flag = True

    def move_to_nearest_road(self):
        """ move to agent nearest white road """

        if(self.right_flag == True):
            if(self.starting_pos_x != self.nearest_road_coords[0] + 10):
                self.starting_pos_x += 1
                self.rect.right += 1
                
        elif(self.left_flag == True):
            if(self.starting_pos_x != self.nearest_road_coords[0] - 10):
                self.starting_pos_x -= 1
                self.rect.right -= 1
                
        elif(self.top_flag == True):
            if(self.starting_pos_y != self.nearest_road_coords[1] - 10):
                self.starting_pos_y -= 1
                self.rect.top -= 1
                
        elif(self.bottom_flag == True):
            if(self.starting_pos_y != self.nearest_road_coords[1] + 10):
                self.starting_pos_y += 1
                self.rect.top += 1

    def update(self):
        """ behavior of an agent at every frame """
        
        self.move_to_nearest_road()
        