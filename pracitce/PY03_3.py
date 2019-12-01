"""
실습: 대소문자 변환 프로그램
-아래 예시과 같이 입력 받은 문자열을 대소문자 변환 후 출력
반복적으로 입력받을 수 있도록 구현하고, 'exit' 입력 시 프로그램 종료
-swapcase() 함수 사용 금지
    <예시>
    문자열 입력 : Hello World
    대소문자 변환 결과 => hELLO wORLD
    문자열 입력 : exit
"""

# 솔루션
while True:  # 반복적으로 입력받을 수 있도록 무한루프
    letter = input("문자열 입력 : ")  # 문자열을 입력받고 letter에 저장
    # 'exit' 입력 시 while 탈출 (프로그램 종료)
    if letter == "exit" :
        break
    # 문자열의 각 문자로부터 소문자일 때 대문자로, 대문자일 때 소문자로 변환 후 출력하고
    # 둘 다 아닐 시 바로 출력한다.
    for i in range(0, len(letter), 1) :
        if letter[i].islower() == True:
            print(letter[i].upper(),end="")
        elif letter[i].isupper() == True:
            print(letter[i].lower(),end="")
        else: print(letter[i],end="")
    print("")

