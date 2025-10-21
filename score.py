from asteroid import Asteroid
from constants import *

class Score:
    def __init__(self):
        self.score = 0

    def update(self, asteroid):
        asteroid.split()
        if asteroid.radius > 2 * ASTEROID_MIN_RADIUS:
            self.score += LARGE_ASTEROID_SCORE
        elif asteroid.radius > 1.25 * ASTEROID_MIN_RADIUS:
            self.score += MEDIUM_ASTEROID_SCORE
        else:
            self.score += SMALL_ASTEROID_SCORE




