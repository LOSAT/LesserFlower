# unused function

import numba

@numba.jit(nopython=True, fastmath=True)
def use_indexizer(height):
    @numba.jit(cache=True, nopython=True, fastmath=True)
    def indexize(x, y):
        return (y * height + x) * 3
    return indexize
    