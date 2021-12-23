import pygame
from math import sqrt
from random import randrange

class Image:

    def select_colored_pixel_coords(self, image) -> list:
        """ select colored pixels coordinates from an image and return list of them """

        colored_pixel_coords = []

        # traverse every pixel on an image
        for x in range(image.get_width()):
            for y in range(image.get_height()):
                if image.get_at((x, y)) != (255, 255, 255, 255):
                    colored_pixel_coords.append((x, y))

        return colored_pixel_coords

    def select_random_colored_pixel_coords(self, colored_pixel_coords) -> tuple:
        """ return random coordinates of colored pixel """

        random_colored_coords = colored_pixel_coords[randrange(len(colored_pixel_coords))]

        return random_colored_coords

    def find_nearest_road_coords(self, agent_coords) -> tuple:
        """ return coordinates of nearest road """

        image = pygame.transform.smoothscale(pygame.image.load("img/map.svg"), (1440, 900))

        right_left_top_bottom_road_distances = [9999, 9999, 9999, 9999]
        right_left_top_bottom_road_coords = [(0, 0), (0, 0), (0, 0), (0, 0)]

        starting_x = agent_coords[0]
        starting_y = agent_coords[1]

        # right
        try:
            current_x = agent_coords[0]
            current_y = agent_coords[1]

            for i in range(image.get_width() - starting_x):
                current_x += 1
                if image.get_at((current_x, current_y)) == (255, 255, 255, 255):
                    distance_right = sqrt((current_x - starting_x)**2 + (current_y - starting_y)**2)
                    right_left_top_bottom_road_distances[0] = distance_right
                    right_left_top_bottom_road_coords[0] = ((current_x, current_y))
                    break

        except:
            pass

        # left
        try:
            current_x = agent_coords[0]
            current_y = agent_coords[1]

            for i in range(starting_x):
                current_x -= 1
                if image.get_at((current_x, current_y)) == (255, 255, 255, 255):
                    distance_left = sqrt((starting_x - current_x)**2 + (current_y - starting_y)**2)
                    right_left_top_bottom_road_distances[1] = distance_left
                    right_left_top_bottom_road_coords[1] = ((current_x, current_y))
                    break

        except:
            pass

        # top
        try:
            current_x = agent_coords[0]
            current_y = agent_coords[1]
        
            for i in range(starting_y):
                current_y -= 1
                if image.get_at((current_x, current_y)) == (255, 255, 255, 255):
                    distance_top = sqrt((starting_x - current_x)**2 + (starting_y - current_y)**2)
                    right_left_top_bottom_road_distances[2] = distance_top
                    right_left_top_bottom_road_coords[2] = ((current_x, current_y))
                    break
        except:
            pass

        # bottom
        try:
            current_x = agent_coords[0]
            current_y = agent_coords[1]

            for i in range(image.get_height() - starting_y):
                current_y += 1
                if image.get_at((current_x, current_y)) == (255, 255, 255, 255):
                    distance_bottom = sqrt((starting_x - current_x)**2 + (current_y - starting_y)**2)
                    right_left_top_bottom_road_distances[3] = distance_bottom
                    right_left_top_bottom_road_coords[3] = ((current_x, current_y))
                    break
        except:
            pass

        min_distance = min(right_left_top_bottom_road_distances)
        min_distance_index = right_left_top_bottom_road_distances.index(min_distance)
        nearest_road_coords = right_left_top_bottom_road_coords[min_distance_index]

        return (nearest_road_coords, min_distance_index)