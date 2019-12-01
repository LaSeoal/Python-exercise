"""
실습: 사진 보기 프로그램
-5장의 사진
-"<<이전", "다음>>"버튼을 눌러 이전, 다음 이미지 보여줌
    -마지막 사진에서 다음(Right)을 누르면 첫 번째 사진 보여줌
    -첫 번째 사진에서 이전(Left)을 누르면 마지막 사진 보여줌
"""

# 솔루션
from tkinter import *

# "<<이전" 버튼 액션 구현 함수
def left_func():
    if image_num[0]>1 :  # 현재 사진이 첫 번째 사진이 아닐 때 사진 인덱스를 1감소시킨다.
        image_num[0]-=1
    else :  # 현재 사진이 첫 번째 사진일 때 사진 인덱스를 마지막 숫자인 5로 바꾼다.
        image_num[0]=5
    # 감소시킨 인덱스에 따라 이미지를 이전 이미지로 바꾸고 화면에 출력한다.
    image = PhotoImage(file = "jeju" + str(image_num[0]) + ".gif")
    la_image.configure(image=image)
    la_image.image = image
# "다음>>" 버튼 액션 구현 함수
def right_func():
    if image_num[0] < 5:  # 현재 사진이 마지막 번째 사진이 아닐 때 사진 인덱스를 1증가시킨다.
        image_num[0] += 1
    else:  # 현재 사진이 마지막 번째 사진일 때 사진 인덱스를 첫번째 숫자인 1로 바꾼다.
        image_num[0] = 1
    # 증가시킨 인덱스에 따라 이미지를 다음 이미지로 바꾸고 화면에 출력한다.
    image = PhotoImage(file="jeju" + str(image_num[0]) + ".gif")
    la_image.configure(image=image)
    la_image.image = image

image_num = []
image_num.append(1)

win = Tk()
win.title("사진 앨범 보기")
# 이전, 다음 버튼 생성과 버튼 액션 구현 함수 설정
btn_left = Button(win, text="<<이전", command=left_func)
btn_right = Button(win, text="다음>>", command=right_func)
# 버튼을 화면에 삽입
btn_left.grid(row=0, column=0)
btn_right.grid(row=0, column=1)
# 이미지를 화면에 삽입
la_image = Label(win)
la_image.grid(row=1, columnspan=2)
image = PhotoImage(file = "jeju1.gif")
la_image.configure(image=image)

win.mainloop()