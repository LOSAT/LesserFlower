# 참고사항

몇 가지 환경 종속적 문제를 해결하기 위해 Windows에서는 GLUT,  
Mac에서는 GLFW를 사용하고 있었으나 양쪽 모두 GLFW를 사용하도록 수정하였습니다.

## 변경점

Windows와 Mac에서 모두 동일한 기능을 사용 가능하도록 구성하고 있으나 렌더링 관련 문제를 해결하기 위해 Mac에서는 몇 가지 코드를 수정하거나 추가해야 합니다. 

### 렌더링이 화면 좌측 하단 (1 / 4)에서만 수행되는 현상


[line 13:](https://github.com/LOSAT/LesserFlower/blob/master/src/mac/main.py#L13) 사용될 픽셀의 전체 크기를 2배로 키웁니다.    

[line 136~137:](https://github.com/LOSAT/LesserFlower/blob/master/src/mac/main.py#L136-L137) 사용될 픽셀의 전체 크기를 2배로 키웁니다.  

[line 146:](https://github.com/LOSAT/LesserFlower/blob/master/src/mac/main.py#L146) 창의 크기를 1/2배로 설정합니다.  

[line 153~156:](https://github.com/LOSAT/LesserFlower/blob/master/src/mac/main.py#L153-L156) `get_framebuffer_size()`를 사용하여 프레임 버퍼의 크기를 계산한 뒤, `glViewPort()`를 통해 렌더링 영역을 중앙으로 조정합니다.

