# 모든 물질 관련 구현은 이 양식을 지켜야 함

import numba
from lib.matter.Particle import Particle

class CustomMatter(Particle):
    def __init__(self) -> None:
        super().__init__()
        self.type = 'matter-own-type' # readonly


@numba.jit(nopython=True, fastmath=True)
def update_custom_matter(entity, time):
    ...