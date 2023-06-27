from tkinter import *
from tkinter import messagebox

# 함수 정의 
# def myFunc() :
#     messagebox.showinfo("다이얼로그 제목 창입니다!","다이얼로그 내용 창입니다.")

def myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("","체크버튼이 꺼졌어요")
    else :
        messagebox.showinfo("","체크버튼이 켜졌어요")

window = Tk()
window.title("윈도창 연습")
# window.geometry("500x400")
# window.resizable(width=False, height=False)

label1 = Label(window, text = "COOKBOOK, 데이터 분석을")
label2 = Label(window, text = "열심히", font=("궁서체",30), fg = "blue")
label3 = Label(window, text = "공부 중입니다.", bg="magenta",
               width=20, height=5, anchor=SE)

photo = PhotoImage(file="gif/dog.gif")
photo2 = PhotoImage(file="gif/cat.gif")
photo3 = PhotoImage(file="gif/cat2.gif")
labelImg = Label(window, image=photo)
labelImg2 = Label(window, image=photo2)
labelImg3 = Label(window, image=photo3)

button1 = Button(window, text="종료버튼",fg="red", command=quit)
button1.pack()

button2 = Button(window, image=photo3, command=myFunc)
button2.pack()


chk = IntVar
cb1 = Checkbutton(window, text="클릭하세요", variable=chk, command=myFunc)
cb1.pack


# labelImg.pack(side=LEFT)
# labelImg2.pack(side=RIGHT)
# labelImg3.pack()

# label1.pack()
# label2.pack()
# label3.pack()


window.mainloop()
