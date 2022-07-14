# 참고사항

Lesser Flower의 기존 엔진은 OpenGL과 GLUT을 사용하여 Windows에서 작성되었으나 몇 가지 문제로 Mac에서의 작동이 원활하지 않아 임시로 개발 환경을 조정하여 구성하였습니다.  

본 문서에서는 Windows와 Mac에서 각각 어떤 부분이 교체되었고 달라진 점은 무엇인지 서술합니다.


## API (GLUT -> GLFW)

> Windows를 원본으로 삼아 Mac에서 변경된 점을 기술합니다.


|GLUT|GLFW|상세|
|:--:|:--:|:--:|
|`glutInit`|`init`|-|
|`glutInitDisplayMode`|-|삭제됨|
|`glutInitWindowSize`|-|`create_window`에서 담당|
|`glutCreateWindow`|`create_window`|`make_context_current`와 사용|
|`glutDisplayFunc`|-|삭제됨|
|`glutMotionFunc`|`set_cursor_pos_callback`|-|
|`glutMainLoopEvent`|-|`window_should_close`와 `poll_events`, `terminate`를 사용하여 구현|
|`glutSwapBuffers`|`swap_buffers`|-|

## 동작

기능 부분에서는 동일하게 작동하도록 작성하지만 일부 문제를 해결하기 위해 추가적인 코드가 필요합니다.  

현재까지 확인된 문제는 다음과 같습니다.

### 렌더링이 화면 좌측 하단 (1 / 4)에서만 수행되는 현상

`get_framebuffer_size()`를 사용하여 프레임 버퍼의 크기를 계산한 뒤
렌더링 영역을 `glViewPort()`를 통해 중앙으로 조정합니다.  

이후 렌더링 영역의 크기를 창 크기 전체로 확대하기 위해 width및 height를 각각 2배로 키우고, 창 생성 당시에는 키우기 전 값으로 적용합니다.
