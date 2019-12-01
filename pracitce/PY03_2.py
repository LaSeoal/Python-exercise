"""
실습: 리스트에서 특정 요소 선택하기
-여러개의 문자열로 구성된 리스트 a (코드 내부에 정의)
    a = ["alpha", "beta", "gamma", "delta", "epsilon", "zeta"]
-사용자로부터 선택할 문자열 길이(정수) 입력받음
-문자열 중 입력된 숫자 길이의 문자 선택
    문자열 길이 함수 : len(문자열)
-선택된 문자들을 리스트 형태로 출력
"""

# 솔루션
a = ["alpha","beta","gamma","delta","epsilon","zeta"]  # 리스트 a 정의
length = int(input("문자열 길이 : "))  # 문자열 길이를 정수형으로 입력받아 length에 저장
b = []
for i in range(0, len(a), 1):
    if len(a[i]) == length :  # 리스트의 i번째 요소의 길이가 입력받은 length와 같으면
        b.append(a[i])  # 리스트 b에 리스트 a의 i번째 요소를 추가한다
print(b)