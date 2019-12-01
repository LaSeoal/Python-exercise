"""
실습: 입력 문자 뷰어
-윈도우 메뉴)
    -File
        -Input String : SimpleDialog 에서 문자 입력
        -Exit : 프로그램 종료
-Radio Group 1) 배경색 3가지
-Radio Group 2) 글자색 3가지
-Label) 입력된 문자 출력
    -Radio Button 선택에 따라 출력 색상 변경
"""

# 솔루션
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
from tkinter.simpledialog import *
# 윈도우 메뉴에서 문자를 입력받는 함수
def func_input():
    input_str = askstring("String", "문자를 입력하세요")
    la_str.configure(text=str(input_str), width=20, height=2)
# 윈도우 메뉴에서 프로그램을 종료하는 함수
def func_exit():
    win.quit()
    win.destroy()
# 배경색과 글자색을 바꾸는 라디오 버튼 함수
def radio_func():
    if bgcolor.get()==1 :
        la_str.configure(bg="blue")
    elif bgcolor.get()==2 :
        la_str.configure(bg="black")
    elif bgcolor.get()==3 :
        la_str.configure(bg="yellow")

    if fgcolor.get()==4 :
        la_str.configure(fg="white")
    elif fgcolor.get()==5 :
        la_str.configure(fg="yellow")
    elif fgcolor.get()==6 :
        la_str.configure(fg="red")

# 메인코드
# 창 구현
win = Tk()
win.title("Viewer Photo")
win.resizable(width=False, height=False)
# 메뉴 공간 구현
main_menu = Menu(win)
win.config(menu=main_menu)

menu1_file = Menu(main_menu)
# File 메뉴 구현
main_menu.add_cascade(label="File", menu=menu1_file)
# 서브 메뉴 구현
menu1_file.add_command(label="Input String", command=func_input)
menu1_file.add_separator()
menu1_file.add_command(label="Exit", command=func_exit)

bgcolor = IntVar()
fgcolor = IntVar()
# 라벨과 라디오 버튼을 생성하고 버튼 액션 함수 설정.
la_bg = Label(win, text="<배경색>")
rb1 = Radiobutton(win, text="blue", variable=bgcolor, value=1, command=radio_func)
rb2 = Radiobutton(win, text="black", variable=bgcolor, value=2, command=radio_func)
rb3 = Radiobutton(win, text="yellow", variable=bgcolor, value=3, command=radio_func)

la_fg = Label(win, text="<글자색>")
rb4 = Radiobutton(win, text="white", variable=fgcolor, value=4, command=radio_func)
rb5 = Radiobutton(win, text="yellow", variable=fgcolor, value=5, command=radio_func)
rb6 = Radiobutton(win, text="red", variable=fgcolor, value=6, command=radio_func)
# 라벨과 라디오 버튼을 창에 삽입.
la_bg.grid(row=0, column=0, padx=40)
la_fg.grid(row=0, column=1, padx=40)
rb1.grid(row=1, column=0, padx=40)
rb2.grid(row=2, column=0, padx=40)
rb3.grid(row=3, column=0, padx=40)
rb4.grid(row=1, column=1, padx=40)
rb5.grid(row=2, column=1, padx=40)
rb6.grid(row=3, column=1, padx=40)

la_str = Label(win)
la_str.grid(row=4, columnspan=2)

win.mainloop()