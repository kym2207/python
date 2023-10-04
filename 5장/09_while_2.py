'''
    작성일 : 2023년 10월 4일
    작성자 : 202395008 김유민
    설명 : 조건에 따라 반복하는 while문
            교재 129 페이지

            1~10까지의 합계를 계산하여 출력하기
            시작 값 : 1
            종료 값 : 10
            증가 값 : 1
            for i in range(1,11): => while문으로
'''
num=1
sum=0

while num <= 10:
    sum=sum+num
    num+=1
print("합계 : ",sum)