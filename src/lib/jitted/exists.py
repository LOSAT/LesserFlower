import numba

@numba.jit(nopython=True, fastmath=True)
def exists(buffer, index):
    return index <= len(buffer)