from tkinter import *

window = Tk()
photo = PhotoImage(file = 'C:/CookAnalysis/GIF/pic7.gif')
h = photo.height()
w = photo.width()
print('이미지 크기 : ', h, 'x', w)

photoR=[ [0 for _ in range(h)] for _ in range(w)] # _는 i,k를 생략한 것
photoG=[ [0 for _ in range(h)] for _ in range(w)]
photoB=[ [0 for _ in range(h)] for _ in range(w)]

for i in range(w) :
    for k in range(h) :
        r, g, b = photo.get(i,k) # 비구조화 할당, 함수 리턴하면 1개, 파이썬 특성 여러개 반환, 타입 튜플
        photoR[i][k] = r
        photoG[i][k] = g
        photoB[i][k] = b

print('[50][50] 위치의 RGB 값 : ', photoR[50][50], photoG[50][50], photoB[50][50] )
