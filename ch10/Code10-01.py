import random
## 파이썬 2차원 리스트 생성
SIZE = 5
SIZE2 = 4
pythonList = [ [random.randint(0,255) for _ in range(SIZE)] for _ in range(SIZE2)]

## 리스트를 출력하기
for i in range(SIZE) :
    for k in range(SIZE) :
        print("%3d" % pythonList[i][k], end=' ')
    print()
print()

## 리스트에 100을 더하기.
# 넘파이 모듈을 사용하기 전에, 이중 리스트 안에 값을 변경할려고 할 때,
# 반복문을 이용하여 변경하는 부분 보여주기
for i in range(SIZE) :
    for k in range(SIZE2) :
        pythonList[i][k] += 100

## 리스트를 출력하기
for i in range(SIZE) :
    for k in range(SIZE2) :
        print("%3d" % pythonList[i][k], end=' ')
    print()