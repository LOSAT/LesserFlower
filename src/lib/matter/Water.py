import numba
import numpy
from lib.matter.Particle import Particle
from lib.math.Point import Point

class Water(Particle):
    def __init__(self) -> None:
        super().__init__(Point(0, 0), (0, 0, 255))
        self.type = 0 # readonly

@numba.jit(cache=True, nopython=True, fastmath=True)
def update_water(entity, time):
    entity[2] = entity[2] + 1
    return entity