import numba

@numba.jit(nopython=True, fastmath=True)
def indexize(width, x, y):
    return (y * width + x) * 3