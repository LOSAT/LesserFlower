import numba
import numpy
from lib.jitted.indexize import indexize

# TODO: 이거 버그나는 이유가 뭘까
@numba.jit(nopython=True)
def pre_render(width, entities, buffer):
    for i in range(entities.size):
        index = indexize(width, entities[i + 1], entities[i + 2])
        buffer[int(index)] = entities[i + 3]
        buffer[int(index + 1)] = entities[i + 4]
        buffer[int(index + 2)] = entities[i + 5]
    return buffer