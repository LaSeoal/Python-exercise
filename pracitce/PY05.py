"""
실습: 주소록 프로그램 1
1. 클래스 구현 (Person, Student, Worker)
-Person 클래스
    -이름, 전화번호 인스턴스 변수
    -이름, 전화번호 반환 메소드
-Student 클래스 (Person 클래스로부터 상속)
    -학과, 학번 인스턴스 변수
    -학과, 학번 반환 메소드
-Worker 클래스 (Person 클래스로부터 상속)
    -부서, 사번 인스턴스 변수
    -부서, 사번 반환 메소드
-Student 또는 Worker 인스턴스 10명 생성
-구분(타입)은 알아서...

2. 메인코드 구현 (주소록 생성 및 출력)
-이름 10개, 전공 및 부서 리스트 코드에 고정
    예시)
    nameList = ["홍동현", "서상욱", "도찬호", "이대희", "최기태", "김동호", "김준식", "이영석", "김승주", "김종범"]
    majorList = ["컴퓨터학부", "경영학부", "통계학과", "기계공학부"]
    departList = ["개발연구팀", "전략기획팀", "인사관리팀"]
-학생과 회사원을 랜덤하게 생성하여 주소록 리스트 생성
    -랜덤하게 생성한 타입에 따라 majorList, departList에서 랜덤하게 생성
    (이름은 순차적으로 가져와도 됨)
    -전화번호 랜덤하게 생성 010-XXXX-XXXX
    -학생일 시 학번 랜덤하게 생성 201XXXXXXX (10자리)
    -회사원일 시 사번 랜덤하게 생성 2019XXX (7자리)
-생성된 전체 주소록 출력 (10명)
    - [학생] 이름: XXX 전화번호: 010-XXXX-XXXX 학과: XXXXX 학번: 201XXXXXXX
    - [사원] 이름: XXX 전화번호: 010-XXXX-XXXX 부서: XXXXX 사번: 2019XXX
    - ....
-이름으로 검색 -> 전화번호 및 정보 출력
    -'끝' 입력 시까지 여러 번 검색 가능

--------- 주소록 프로그램 -----------
[사원] 이름: 홍동현    전화번호:   010-7181-4937   부서: 개발연구팀   사번: 2019072
[사원] 이름: 서상욱    전화번호:   010-7549-6028   부서: 개발연구팀   사번: 2019072
[사원] 이름: 도찬호    전화번호:   010-8860-8044   부서: 인사관리팀   사번: 2019063
[학생] 이름: 이대희    전화번호:   010-7628-1046   학과: 컴퓨터학부   학번: 2016713443
[사원] 이름: 최기태    전화번호:   010-8956-7281   부서: 전략기획팀   사번: 2019004
[학생] 이름: 김동호    전화번호:   010-9227-6711   학과: 경영학부     학번: 2016248770
[학생] 이름: 김준식    전화번호:   010-9964-8057   학과: 통계학과     학번: 2016482967
[학생] 이름: 이영석    전화번호:   010-9395-7947   학과: 기계공학부   학번: 2015477948
[학생] 이름: 김승주    전화번호:   010-1898-4846   학과: 경영학부     학번: 2017320102
[학생] 이름: 김종범    전화번호:   010-3944-1182   학과: 기계공학부   학번: 2014733284
-------------------------------------
찾을 사람 이름은 ? 홍동현
 전화번호 : 010-7181-4937
 부서: 개발연구팀
 사번: 2019072
찾을 사람 이름은 ? 이대희
 전화번호 : 010-7628-1046
 학과: 컴퓨터학부
 학번: 2016713443
찾을 사람 이름은 ? 이영석
 전화번호 : 010-9395-7947
 학과: 기계공학부
 학번: 2015477948
찾을 사람 이름은 ? 끝
주소록 프로그램을 종료합니다.
"""

# 솔루션
import random

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
    unknown.name = nameList[i]  # 이름을 순서에 따라 할당한다.
    unknown.addr = "010-" + str(random.randint(1000,9999)) + "-" + str(random.randint(1000,9999))  # 랜덤으로 주소를 할당한다.
    # 생성된 사람의 정보를 주소록에 추가한다.
    memList.append(unknown)
# 주소록을 출력한다.
print("---------- 주소록 프로그램 ----------")
for Person in memList:  # 주소록에 있는 사람에 대하여
    if(Person.get_type() == "[학생]"):  # 학생이면 학생의 정보를 출력한다.
        print(Person.get_type() + " 이름: " + Person.get_name() + " \t전화번호: " + Person.get_addr() + " \t학과: " + Person.get_major() + "\t학번: " + str(Person.get_stdnum()))
    else:  # 사원이면 사원의 정보를 출력한다.
        print(Person.get_type() + " 이름: " + Person.get_name() + " \t전화번호: " + Person.get_addr() + " \t부서: " + Person.get_dpt() + "\t사번: " + str(Person.get_wknum()))
print("--------------------------------------")
# '끝'을 입력할 때까지 이름을 검색한다.
search = ""
while(search != "끝"):
    search = input("찾을 사람 이름은 ? ")
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

print("주소록 프로그램을 종료합니다.")




