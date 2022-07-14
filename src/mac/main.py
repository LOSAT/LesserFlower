import numba as nb
import numpy as np
from OpenGL.GL import *
from numpy.random import randint
import math
from glfw import *
import sys
import os
try:
    del os.environ['DISPLAY']
except:
    pass
windowsize = (800 * 2, 600 * 2)

__buffer = np.zeros(windowsize[0] * windowsize[1] * 3)


@nb.jit()
def iterBuff(buffer, func):
    for i, v in enumerate(buffer):
        buffer[i] = func(i, v)
    return buffer


def create_buffer_editor(callback):
    @nb.jit(nopython=True)
    def func(buffer):
        for i, v in enumerate(buffer):
            buffer[i] = callback(i, v)
        return buffer
    return func
 
@nb.jit(nopython=True, fastmath=True)
def control(i, v):
    pass
iterBuffer = create_buffer_editor(control)

@nb.jit(nopython=True, fastmath=True)
def update_process(i, v):
    pass
update_buffer = create_buffer_editor(update_process)


@nb.jit(nopython=True, fastmath=True)
def has(vec, val):
    res = False
    if np.where(vec == val)[0].shape[0] > 0:
        res = True
    return res
set

@nb.jit(nopython=True, fastmath=True)
def idx(x, y):
    return (y * windowsize[0] + x) * 3

def fill_water(x, y):
    if(idx(x, y) < len(__buffer)):
        __buffer[idx(x, y)] = 0
        __buffer[idx(x, y) + 1] = 0
        __buffer[idx(x, y) + 2] = 255


@nb.jit(nopython=True, fastmath=True)
def validate_frag(buffer, base_index, rgb):
    return (
        buffer[base_index] == rgb[0] 
        and buffer[base_index + 1] == rgb[1] 
        and buffer[base_index + 2] == rgb[2]
    )

@nb.jit(nopython=True, fastmath=True)
def is_fragment_empty(buffer, index):
    return validate_frag(buffer, index, (0, 0, 0))


@nb.jit(nopython=True, fastmath=True)
def exists(buffer, index):
    return index <= len(buffer)

@nb.jit(nopython=True, fastmath=True)
def update_water(time, buffer, sandy): # sandy는 테스트
    mem = np.zeros(windowsize[0] * windowsize[1] * 3) # 한 번만 업데이트하게 하기 위함(255가 아니여도 된다.). 비효율적이므로 수정 ㄱ
    for y in range(windowsize[1]):
        for x in range(windowsize[0]):
            
            current = idx(x, y)
            down = idx(x, y + 1)
            left_down = idx(x - 1, y + 1)
            right_down = idx(x + 1, y + 1)
            left = idx(x - 1, y)
            right = idx(x + 1, y)

            if(exists(buffer, down + 2) and mem[current] == 0): # 주기 정하려면 time % ms == 0 추가, 한 번만 업데이트하게 하기 위함. 비효율적이므로 수정 ㄱ
                is_blue = validate_frag(buffer, current, (0, 0, 255))
                if(is_blue and is_fragment_empty(buffer, down)):
                    mem[down] = 255
                    buffer[down + 2] = 255 # 아래 채우기
                    buffer[current + 2] = 0 # 현재 위치 지우기

                elif(is_blue and is_fragment_empty(buffer, left_down)):
                    mem[left_down] = 255
                    buffer[left_down + 2] = 255
                    buffer[current + 2] = 0

                elif(is_blue and is_fragment_empty(buffer, right_down)): # 고체 가루와 비슷..
                    mem[right_down] = 255
                    buffer[right_down + 2] = 255
                    buffer[current + 2] = 0
        
                elif(is_blue and is_fragment_empty(buffer, right) and not sandy): # 부터는 액체의 특성을 가짐
                    mem[right] = 255
                    buffer[right + 2] = 255
                    buffer[current + 2] = 0    

                elif(is_blue and is_fragment_empty(buffer, left) and not sandy):
                    mem[left] = 255
                    buffer[left + 2] = 255
                    buffer[current + 2] = 0   

water_fill_range = 100
def on_drag(x, y):
    fill_water(x, y)

    for i in range(100):
        fill_water(x + randint(-water_fill_range, water_fill_range), y + randint(-water_fill_range, water_fill_range))

click = False
def on_click(window, button ,action, asdf):
    global click
    if(button == MOUSE_BUTTON_LEFT):
        if(action == PRESS):
            click = True
        elif(action == RELEASE):
            click = False
def on_move(window, x, y):
    x = 2 * x
    y = 2 * y
    if(click):
        fill_water(math.floor(x), math.floor(y))

        for i in range(10):
            fill_water(math.floor(x) + randint(-water_fill_range, water_fill_range), math.floor(y) + randint(-water_fill_range, water_fill_range))
def main():
    time = 0
    init()
    window = create_window(windowsize[0] // 2, windowsize[1] // 2, "Lesser Flower", None, None)
    make_context_current(window)
    #glutMouseFunc(on_click)
    set_mouse_button_callback(window, on_click)
    set_cursor_pos_callback(window, on_move)
    #glutPassiveMotionFunc()

    fb_width, fb_height = get_framebuffer_size(window)
    _x = -(windowsize[0] - fb_width) // 2
    _y = -(windowsize[1] - fb_height) // 2
    glViewport( _x, _y, windowsize[0], windowsize[1])
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho( 0, windowsize[0], 0, windowsize[1], 0, 10)
    glPixelZoom( 1, -1 )
    glRasterPos3f(0, windowsize[1], -0.3)
    while not window_should_close(window):
        glClearColor(0, 0, 0, 255)
        glClear(GL_COLOR_BUFFER_BIT)
        #newBuffer = update_buffer(__buffer)
        update_water(time, __buffer, False)
        
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
        glPixelStorei(GL_UNPACK_SKIP_PIXELS, 0)
        glPixelStorei(GL_UNPACK_SKIP_ROWS, 0)
        glDrawPixels(*windowsize, GL_RGB, GL_UNSIGNED_BYTE, __buffer) # 임시로 __buffer를 전역으로 직접 수정하게끔 함.
        # 단, JIT 처리된 함수는 인자로 받아 수정
        swap_buffers(window)
        poll_events()
        time = time + 1 # 프레임 처리를 위함
    terminate()

main()
