import numba
import numpy
from lib.jitted.indexize import indexize

# TODO: 이거 버그나는 이유가 뭘까
@numba.jit(nopython=True)
def pre_render(width, height, entities, buffer):
    for _i in range(entities.size // 6):
        i = _i * 6 
        index = indexize(width, entities[i + 1], entities[i + 2])
        buffer[index] = entities[i + 3]
        buffer[index + 1] = entities[i + 4]
        buffer[index + 2] = entities[i + 5]
    return buffer