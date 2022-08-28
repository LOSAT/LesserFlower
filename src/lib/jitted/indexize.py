import numba

@numba.jit(cache=True, nopython=True, fastmath=True)
def indexize(width, x, y):
    return (y * width + x) * 3