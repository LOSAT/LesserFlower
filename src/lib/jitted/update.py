import numba
import numpy
from lib.jitted.exists import exists
from lib.jitted.indexize import indexize
from lib.jitted.is_fragment_empty import is_fragment_empty
from lib.matter.Water import update_water


@numba.jit(nopython=True, fastmath=True)
def update_entity(entities, buffer, time): #중간에 변속되는듯한 느낌 해결해야됨
    for _i in range(entities.size // 6): #하드코딩 (일시적)
        i = _i * 6
        if entities[i] == 0: 
            x = entities[i + 1]
            y = entities[i + 2]

            current = indexize(800, x, y)
            down = indexize(800, x, y + 1)
            left_down = indexize(800, x - 1, y + 1)
            right_down = indexize(800, x + 1, y + 1)
            left = indexize(800, x - 1, y)
            right = indexize(800, x + 1, y)

            if exists(buffer, down + 2) and is_fragment_empty(buffer, down):
                buffer[current + 2] = 0 # 이거 안 해도 알아서 갱신해줘야 정상인데..
                entities[i + 2] = entities[i + 2] + 1
    return entities