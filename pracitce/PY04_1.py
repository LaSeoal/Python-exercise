"""
실습: 최저, 최고, 평균 점수내기
-여러 과목의 점수를 한꺼번에 입력 (과목 수는 변동 가능)
    -점수는 실수 (소수점 가능)
    -','를 기준으로 분리
    -99999 입력 시 종료 (여러 번 수행 가능하도록 구현)
- 입력 받은 점수 중 최저, 최고 점수를 동시에 반환하는 함수 생성
    -최저점수, 최고점수 = get_minmax(...)
- 입력 받은 점수의 평균 점수를 반환하는 함수 생성
    -평균점수 = get_average(...)
- 최종 결과 출력은 각 점수별 소수점 2자리까지 출력

교과목들의 점수를 한꺼번에 입력하세요: 9.1,28.2,58,97,15.7
최저점수: 9.10, 최고점수: 97.00, 평균점수: 41.60
교과목들의 점수를 한꺼번에 입력하세요: 99,21.6,57.9
최저점수: 21.60, 최고점수: 99.00, 평균점수: 59.50
교과목들의 점수를 한꺼번에 입력하세요: 99999
"""

# 솔루션

# 점수 중 최저, 최고 점수를 동시에 반환하는 함수
def get_minmax(score) :
    score_s = sorted(score)  # 입력받은 점수를 오름차순 정렬한다.
    min = score_s[0]  # 정렬된 리스트의 첫번째 요소가 최솟값이다.
    max = score_s[len(score_s)-1]  # 정렬된 리스트의 마지막 요소가 최댓값이다.
    return min,max
# 점수의 평균 점수를 반환하는 함수
def get_average(score) :
    sum=0
    # 각 점수를 모두 더한다.
    for i in range(0, len(score), 1):
        sum=sum+score[i]
    return sum/len(score)  # 점수의 총합에 점수의 개수만큼 나누면 평균값이다.

# 메인코드
while(1) :
    # 점수를 콤마로 구분하여 입력받아서 실수형으로 매핑하여 리스트에 저장한다.
    score = list(map(float,input("교과목들의 점수를 한꺼번에 입력하세요: ").split(',')))
    # 99999가 입력되면 무한루프를 탈출한다(프로그램 종료).
    if score[0]==99999 :
        break
    # 위에서 구현한 함수를 사용하여 최저, 최고, 평균 점수를 구하고 출력한다.
    minmax = get_minmax(score)
    ave = get_average(score)
    print("최저점수: %.2f, 최고점수: %.2f, 평균점수: %.2f" % (minmax[0],minmax[1], ave))





