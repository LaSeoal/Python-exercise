"""
실습: 주소록 프로그램2 (주소록 파일 읽기, 로그파일 쓰기)
-주소록 랜덤 생성 부분->address.txt파일에서 읽어서 주소록 생성
(address.txt파일 수정해도 됨. 예시 '이름:'삭제)
-Student/Worker 클래스, 검색 등은 그대로 사용)
-"address.log"파일 생성 및 쓰기
-log 파일에는 프로그램 수행 동작들을 시간별로 남김 (time 모듈 사용)
    -주소록 파일 open
    -주소록 생성 완료 (명 수)
    -이름으로 검색
    -프로그램 종료
"""

# 솔루션
import random
import time

out_file = None
log_file = None
# Person 클래스
class Person:
    # 이름, 전화번호, 타입 변수 초기화
    def __init__(self, name, addr, type):
        self.name = name
        self.addr = addr
        self.type = type
    # 각 변수에 대한 게터(getter)함수 정의
    def get_name(self):
        return self.name
    def get_addr(self):
        return self.addr
    def get_type(self):
        return self.type
# Student 클래스
class Student(Person):
    # 전공, 학번 변수 초기화
    def __init__(self, major, stdnum):
        self.major = major
        self.stdnum = stdnum
    # 각 변수에 대한 게터(getter)함수 정의
    def get_major(self):
        return self.major
    def get_stdnum(self):
        return self.stdnum
# Worker 클래스
class Worker(Person):
    # 부서, 사번 변수 초기화
    def __init__(self, dpt, wknum):
        self.dpt = dpt
        self.wknum = wknum
    # 각 변수에 대한 게터(getter)함수 정의
    def get_dpt(self):
        return self.dpt
    def get_wknum(self):
        return self.wknum

# 메인코드
# 이름, 전공, 부서 리스트를 초기화한다.
nameList = ["홍동현", "서상욱", "도찬호", "이대희", "최기태", "김동호", "김준식", "이영석", "김승주", "김종범"]
majorList = ["컴퓨터학부", "경영학부  ", "통계학과  ", "기계공학부"]
departList = ["개발연구팀", "전략기획팀", "인사관리팀"]
memList = []
# 주소록 파일과 로그 파일을 생성
log_file = open("address.log", 'w')
out_file = open("address.txt", 'w')
# 주소록 파일 open 시각을 로그 파일에 기록
log_file.write('[' + time.asctime() + "] ")
log_file.write("open file address.txt\n")
# 임의의 사람 10명에 대하여 학생/사원 여부와 정보를 랜덤으로 결정한다.
for i in range(10):
    t = random.randint(0,1)  # 랜덤으로 학생/사원 여부를 결정한다. (0: 학생, 1: 사원)
    if(t == 0) :  # 학생 정보 초기화
        # 랜덤으로 전공과 학번을 할당한다.
        unknown = Student(majorList[random.randint(0,3)], random.randint(2010000000, 2019999999))
        unknown.type = "[학생]"  # 학생 타입을 부여
    else :  # 사원 정보 초기화
        # 랜덤으로 부서와 사번을 할당한다.
        unknown = Worker(departList[random.randint(0,2)], random.randint(2019000,2019999))
        unknown.type = "[사원]"  # 사원 타입을 부여
    # 학생,사원의 공통 정보를 할당한다.
    unknown.name = nameList[i]
    unknown.addr = "010-" + str(random.randint(1000,9999)) + "-" + str(random.randint(1000,9999))
    # 생성된 사람의 정보를 주소록에 추가한다.
    memList.append(unknown)
# 주소록을 출력한다.
print("---------- 주소록 프로그램 ----------")
for Person in memList:  # 주소록에 있는 사람에 대하여
    if(Person.get_type() == "[학생]"):  # 학생이면 학생의 정보를 출력한다.
        print(Person.get_type() + " 이름: " + Person.get_name() + " \t전화번호: " + Person.get_addr() + " \t학과: " + Person.get_major() + "\t학번: " + str(Person.get_stdnum()))
        # 학생 정보를 주소록 파일에 기록한다.
        out_file.write(Person.get_type() + '\t' + Person.get_name() + '\t' + Person.get_addr() + '\t' + Person.get_major() + " \t" + str(Person.get_stdnum()))
        out_file.write('\n')
    else:  # 사원이면 사원의 정보를 출력한다.
        print(Person.get_type() + " 이름: " + Person.get_name() + " \t전화번호: " + Person.get_addr() + " \t부서: " + Person.get_dpt() + "\t사번: " + str(Person.get_wknum()))
        # 사원 정보를 주소록 파일에 기록한다.
        out_file.write(Person.get_type() + '\t' + Person.get_name() + '\t' + Person.get_addr() + '\t' + Person.get_dpt() + " \t" + str(Person.get_wknum()))
        out_file.write('\n')
print("--------------------------------------")
# 주소록 생성 완료를 로그 파일에 기록
log_file.write('[' + time.asctime() + "] ")
log_file.write("total 10 persons\n")
out_file.close()

# '끝'을 입력할 때까지 이름을 검색한다.
search = ""
while(search != "끝"):
    search = input("찾을 사람 이름은 ? ")
    # 이름 검색을 로그 파일에 기록
    if(search != "끝"):
        log_file.write('[' + time.asctime() + "] ")
        log_file.write("search \"" + search + "\"\n")
    f = 0
    for i in range(0, len(nameList), 1):
        # 찾을 사람 이름이 주소록의 이름 명단에 있을 때
        if(search == nameList[i]):
            f = 1
            print("전화번호 : " + memList[i].get_addr())  # 공통 정보인 주소를 출력한다.
            if(memList[i].get_type() == "[학생]"):  # 찾을 사람이 학생일 때 정보를 출력한다.
                print("학과: " + memList[i].get_major())
                print("학번: " + str(memList[i].get_stdnum()))
            else:  # 찾을 사람이 사원일 때 정보를 출력한다.
                print("부서: " + memList[i].get_dpt())
                print("사번: " + str(memList[i].get_wknum()))
        continue
    # 찾을 사람 이름이 주소록의 이름 명단에 없을 때
    if(f == 0 and search != "끝"):
        print("이름을 찾지 못했습니다.")
# 프로그램 종료를 로그 파일에 기록
log_file.write('[' + time.asctime() + "] ")
log_file.write("exit")
log_file.close()
print("주소록 프로그램을 종료합니다.")
