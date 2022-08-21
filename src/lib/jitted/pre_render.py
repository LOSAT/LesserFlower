import numba
from lib.jitted.indexize import indexize

@numba.jit(cache=True, nopython=True, fastmath=True)
def pre_render(height, entities):
    R = []
    for entity in entities:
        index = indexize(height, entity[1], entity[2])
        R[index] = entity[3][0]
        R[index + 1] = entity[3][1]
        R[index + 2] = entity[3][2]
    return R