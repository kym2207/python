'''
    작성일 : 2023년 10월 11일
    작성자 : 202395008 김유민
    설명 : 여러개의 값을 넘겨주고 여러개의 값을 돌려 받기.

    두 수를 전달하여 사칙 연산의 결과값을 돌려주는 함수
    [알고림즘]
    (함수)
        3. 두수를 전달받아 매개변수에 저장한다.
        4. 두수의 사칙연산(+,-,*,/,%)을 호출한곳으로 돌려준다.
    (메인)
        1. 두 수를 입력 받는다.
        2. 두 수를 가지고 힘수를 호출한다.
        5. 돌려받은 사칙연산(+,-,*,/,%)을 출력한다
'''
#함수 선언
def calc(num1,num2):    # 전달 받은 2개의 값을 저장할 매개변수 2개.
    return num1+num2,num1-num2,num1*num2,num1/num2,num1%num2    #계산한값을 돌려준다

#메인
num1=int(input("첫 번쨰 수 입력 : "))
num2=int(input("두 번쨰 수 입력 : "))

sum, minus, mul, div, rest = calc(num1,num2)
print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {minus}")
print(f"{num1} x {num2} = {mul}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} % {num2} = {rest}")