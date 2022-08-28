import numba
import numpy
from lib.matter.Water import update_water


@numba.jit(cache=True, nopython=True, fastmath=True)
def update_entity(entities, time):
    for i in range(entities.size):
        if entities[i] == 0:
            data = update_water([
                entities[i],
                entities[i + 1],
                entities[i + 2],

                entities[i + 3],
                entities[i + 4],
                entities[i + 5]
            ], time)
            entities[i] = data[0]
            entities[i + 1] = data[1]
            entities[i + 2] = data[2]

            entities[i + 3] = data[3]
            entities[i + 4] = data[4]
            entities[i + 5] = data[5]
    return entities