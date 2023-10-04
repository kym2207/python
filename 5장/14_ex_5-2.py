'''
    작성일 : 2023년 10월 4일
    작성자 : 202395008 김유민
    설명 : 두 수를 입력 받아
            1. 두수 사이의 합계 출력하기
            2. 두 수 사이의 짝수의 합계 출력하기
'''
su1=int(input("시작 정수 입력:"))
su2=int(input("끝 정수 입력:"))
sum1=0
sum2=0
if su1<su2:
    for i in range(su1,su2+1):#시작 정수부터 끝 정수까지 반복
        sum1+=i
        if i%2==0:#짝수일 경우
            sum2+=i
else:
    for i in range(su2,su1+1):#시작 정수부터 끝 정수까지 반복
        sum1+=i
        if i%2==0:#짝수일 경우
            sum2+=i

print(f"{su1}에서 {su2}사이 정수의 합 : {sum1}")
print(f"{su1}에서 {su2}사이 짝수인 정수의 합 : {sum2}")
        
