import turtle
import random

# 함수 선언 부분
def screenLeftClick(x,y) : 
    global r,g,b
    rAngle = random.randrange(1,360)
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    turtle.pencolor((r,g,b)) 
    turtle.pendown()
    turtle.right(rAngle)
    turtle.stamp()
    turtle.goto(x,y)

def screenRightClick(x,y) : 
    global r,g,b
    turtle.pencolor((r,g,b)) 
    turtle.penup()
    turtle.goto(x,y)

def screenMidleClick(x,y) :
    global r,g,b 
    tSize = random.randrange(1,10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

# 변수 선언 부분
pSize = 8
r,g,b = 0.0, 0.0, 0.0

# 메인 코드 부분 
image_path = "c:/san1.png"
screen.register_shape(image_path)

screen = turtle.Screen()
image1 = "san1.png"
# screen.addshape(image1)
screen.register_shape(image1)

turtle.title('거북이로 그림 그리기')
turtle.shape('classic')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick,1)
turtle.onscreenclick(screenMidleClick,2)
turtle.onscreenclick(screenRightClick,3)


# 원 색상 채우기
# turtle.fillcolor("hotpink")
# turtle.begin_fill()
# turtle.circle(70)
# turtle.end_fill()

# turtle.color("black", "red")
# turtle.begin_fill()
# turtle.circle(80)
# turtle.end_fill()

turtle.done()