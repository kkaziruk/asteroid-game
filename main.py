import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    # create an object to help track time
    clock = pygame.time.Clock()
    dt = 0
    # creating a surface, 'screen'
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    # choosing a black colour to fill
    color = (0, 0, 0)   
    # creating groups
    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    # adding classes of objects to groups
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    # instantiate player object 
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT)
    asteroid_obj = AsteroidField()

    while True:
        # the program will never run at more than 60 frames per second
        # clock.tick(60) returns the number of milliseconds since the last tick call
        # dt is the number of seconds for one frame
        dt = clock.tick(60)/1000
        # update background
        screen.fill(color)
        # rotate image
        for obj in updatables:
            obj.update(dt)
        # draw triangle
        for drw in drawables:
            drw.draw(screen)
        # event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # update display
        pygame.display.flip()

if __name__ == "__main__":
    main()
