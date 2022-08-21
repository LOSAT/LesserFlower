import numba

@numba.jit(cache=True, nopython=True, fastmath=True)
def indexize(height, x, y):
    return (y * height + x) * 3