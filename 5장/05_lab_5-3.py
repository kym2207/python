'''
    작성일 : 2023년9월 27일
    작성자 : 202395008 김유민
    설명 : 터틀 그래픽으로 N각형 도형을 그려보자
    사용자로부터 그리고싶은 도형의 변의 수를 입력받아
    도형을 그린다
'''
import turtle as t

t.shape("turtle")

#펜 이동 - 펜 자국이 남지 않도록 들어서 이동
t.penup()
t.goto(-50,-50)
t.pendown() #이동을 마치면 펜을 내려 놓는다.
for i in range(51):
    #원하는 도형을 입력 받는다. => 변수에 저장
    num=int(t.textinput("도형그리기","몇각형의 도형을 그릴까요?"))

    #도형그리기
    for i in range(num):
        t.forward(100)
        t.left(360/num)


t.done