import numba

from lib.jitted.validate_frag import validate_frag

@numba.jit(nopython=True, fastmath=True)
def is_fragment_empty(buffer, index):
    return validate_frag(buffer, index, (0, 0, 0))