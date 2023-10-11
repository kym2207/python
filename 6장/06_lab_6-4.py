'''
    작성일 : 2023년 10월 11일
    작성자 : 202395008 김유민
    설명 : lab 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수.

    리스트에 10개의 값을 랜덤으로 생성하고
    max 또는 min을 입력 받아 최대, 최소값을 찾아 돌려주는 함수.

    (함수)
            5)두 값을 전달 받아 매개 변수에 저장.
            6)최대값, 최소값을 찾는다.
            7)값을 돌려준다
    (메인)
        1.무한반복
            1)랜덤으로 10~99까지 10개의 수를 리스트로 생성
            2)생선된 리스트 출력
            3)사용자로부터 최대값을 알고 싶은지 최소값을 알고 싶은지 묻는다.
              사용자가 입력할 값은 max 또는 mun
            3)입력박은 max 또는 min과 생선된 리스트를 가지고 함수 호출
            8)돌려 받은 최대값 또는 최소값을 출력한다.
'''
def gatMINMAX(list_data,method='max'):
    min=100
    max=1

    if method == 'max' :
        for i in list_data:
            if i > max:
                max=i
        return max
    elif method == 'min' :
        for i in list_data:
            if i < min:
                min=i
        return min

import random
while True:
    list=random.sample(range(10,99),10)#랜덤으로 10~99까지의 수를 리스트로 생성
    print(list)
    s=input("최댓값을 원하면 max, 최솟값을원하면 min을 입력하시오: ")
    print(gatMINMAX(list,s))