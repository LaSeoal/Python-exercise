"""
실습: 야구게임 프로그램
-컴퓨터가 임의로 세자리 숫자 생성
    -세자리 숫자 안에는 같은 숫자가 존재하지 않음
    (예: 123, 456, 789는 가능 / 202, 999, 887은 불가능)
-사용자는 컴퓨터의 세자리 숫자를 맞출 때까지 숫자 입력
-사용자가 입력한 숫자와 컴퓨터가 생성한 숫자의
    -한 숫자와 자릿수가 모두 일치하면 : 1 strike
    -자릿수는 다르나 입력한 한 숫자가 존재하면 : 1 ball
    -세자리 숫자를 정확히 입력하면 : 3 strike (게임 종료)
-예시) 컴퓨터 생성 숫자  사용자 입력  결과
        573             123         1 strike, 0 ball
                        134         0 strike, 1 ball
                        325         0 strike, 2 ball
                        753         1 strike, 2 ball
                        573         3 strike
-게임 시작 ~ 종료까지 시간 출력

게임을 시작합니다...
[6, 8, 1]
숫자를 입력하세요 : 123
[STRIKE] 0  [BALL] 1
숫자를 입력하세요 : 145
[STRIKE] 0  [BALL] 1
숫자를 입력하세요 : 671
[STRIKE] 2  [BALL] 0
숫자를 입력하세요 : 681
[STRIKE] 3  [BALL] 0
게임을 4 회에서 이겼습니다.
게임 시간은 431 초입니다.
"""

# 솔루션
import random
import time

print("게임을 시작합니다...")
n=range(10)
lst=[]
# 각 자리 숫자가 모두 다를 때 까지 세자리 숫자를 랜덤으로 생성.
while(1) :
    a=random.choice(n)
    b=random.choice(n)
    c=random.choice(n)
    if(a!=b and b!=c and a!=c):
        lst=[a,b,c]
        break

print(lst)
iter=1

# 게임 시작
t1 = time.time()  # 게임 시작 시각 기록
while(1) :
    exp = int(input("숫자를 입력하세요 : "))  # 숫자를 입력
    # 입력받은 세 자리 숫자의 각 자리 수로 구분하여 리스트를 생성한다.
    # (컴퓨터가 생성한 숫자가 리스트 형태이기 때문)
    if(exp<100):
        exp_1 = int(exp%10)
        exp_2 = int(exp/10)
        exp_3 = 0
    else :
        exp_1 = int(exp%10)
        exp_2 = int(exp/10%10)
        exp_3 = int(exp/100)
    exp_lst = [exp_3,exp_2,exp_1]
    strike=0
    ball=0
    # 스트라이크/볼 개수를 판별
    for i in range (0, 3, 1) :
        for j in range (0, 3, 1) :
            # 컴퓨터의 한 숫자와 사용자의 한 숫자가 같을 때
            if(lst[i] == exp_lst[j]):
                # 자릿수까지 같으면 스트라이크+1
                if(i==j):
                    strike+=1
                # 자릿수가 다르면 볼+1
                else: ball+=1
    # 3스트라이크면 게임 종료(루프 탈출)
    # 그렇지 않으면 루프 반복
    if(strike == 3):
        break
    else:
        print("[STRIKE] %d\t[BALL] %d" % (strike,ball))
        iter+=1  # 시도 횟수+1
# 게임 끝
t2=time.time()  # 게임 종료 시각 기록
time_w = int(t2-t1)  # 게임 시간 계산
print("게임을 %d 회에서 이겼습니다.\n게임 시간은 %d 초입니다." % (iter, time_w))

