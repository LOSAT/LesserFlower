# Lesser Flower
> Version 2.0a

<img src="https://user-images.githubusercontent.com/34784356/178954445-aae1e5b5-6df5-4f21-94ef-207abe48ff2d.png" width="600">  

이 프로그램은 Flower 프로그램을 본격적으로 구성하기 전에
액체의 효과적인 구현에 관한 실험을 위해 개발하고 있습니다.

## 하위 문서

- [참고사항](/docs/information.md)
## 설명

~~Lesser Flower는 테스트를 진행하기 위한 환경이기 때문에 높은 수준의 추상화를 기대하기 어렵습니다.~~

모든 코드는 픽셀 데이터를 RGB로 취급하여 작성되었습니다.

## 설치 및 실행

### 필요
- numba
- numpy
- pyopengl
- glfw

### 실행
> 2.0a
```
python src/main.py
```
> 이전 버전 (1.1)
```
python src/old/old.py
```
## 주의사항

~~PyOpenGL에는 GLUT이 누락되어 있습니다.~~  
~~Windows의 경우 PyOpenGL을 pip이 아닌 별도의 방법으로 설치해야 합니다.~~  
~~Windows에서도 GLFW를 사용하는 것으로 통일하였습니다.~~

Windows 및 Mac의 코드를 완전히 통일하였습니다. (1.1버전)


## 버전 히스토리

- 1.0 - (2022.7.14)
- 1.1 - (2022.7.17)
- 2.0a - (2022.8.22)