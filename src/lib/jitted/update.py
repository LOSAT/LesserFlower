import numba
from lib.matter.Water import update_water

# TODO: setitem 오류 고치기
@numba.jit(cache=True, nopython=True, fastmath=True)
def update_entity(entities, time):
    R = [
        [
            0,
            0,
            0,
            (0, 0, 0)
        ]
    ]
    for i, entity in enumerate(entities):
        if entity[0] == "water":
            R[i] = update_water(entity, time)
    return R[1:]