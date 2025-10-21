import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
from shots import Shot
from score import Score

def write(screen, font, c_score,location,color=(255,255,255)):
    text = f"Score: {c_score}"
    screen.blit(font.render(text,True,color),location)

def main():
    pygame.init()
    pygame.font.init()
    font=pygame.font.Font(None,30)
    disp_score = 0
    pygame.font.SysFont("Inkfree", 60)
    # create an object to help track time
    clock = pygame.time.Clock()
    dt = 0
    # creating a surface, 'screen'
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Asteroid Game')
    # choosing a black colour to fill
    color = (0, 0, 0)   
    bg_img = pygame.image.load('background.jpg')
    bg_img = pygame.transform.scale(bg_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
    # creating groups
    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # adding classes of objects to groups
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)
    # instantiate player object 
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    # instantiate asteroid object
    asteroid_obj = AsteroidField()
    # instantiate score object
    curr_score = Score()

    while True:
        # the program will never run at more than 60 frames per second
        # clock.tick(60) returns the number of milliseconds since the last tick call
        # dt is the number of seconds for one frame
        dt = clock.tick(60)/1000
        # update background
        screen.fill(color)
        screen.blit(bg_img, (0,0))
        # update score
        write(screen, font, disp_score, (0,0))
        # collisions
        for asteroid in asteroids:
            if asteroid.collision(player):
                sys.exit("Game over!")
            for shot in shots:
                if asteroid.collision(shot):
                    curr_score.update(asteroid)
                    disp_score = curr_score.score
                    shot.kill()
        # update score
        write(screen, font, disp_score, (0,0))
        # update asteroid/player/shot
        for obj in updatables:
            obj.update(dt)
        # draw asteroid/player/shot
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
