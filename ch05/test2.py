from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import *
from tkinter.filedialog import *

# 함수 정의
def func_open() :
    messagebox.showinfo("메뉴 선택","열기 메뉴를 선택함")

def func_exit() :
    window.quit()
    window.destroy()

window =  Tk()

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="열기", command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=func_exit)

label1 = Label(window,text="입력된 값")
label1.pack()
value = askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue=1, maxvalue=6)
label1.configure(text=str(value))

label2 = Label(window,text="선택된 파일 이름")
label2.pack()

filename = askopenfilename(parent=window, \
                           filetypes=(("GIF파일","*gif"),("모든 파일","*.*")))

# label2.configure(text=str(filename))

saveFp = asksaveasfile(parent=window, mode="w", defaultextension=".jpg", \
                       filetypes=(("JPG파일","*.jpg;*jpeg"),("모든 파일","*.*")))
label2.configure(text=saveFp)
saveFp.close()
window.mainloop()