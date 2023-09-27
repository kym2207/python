'''
    작성일 : 2023년9월 27일
    작성자 : 202395008 김유민
    설명 : 터틀 그래픽으로 여러개의 원을 그려보자
'''
import turtle as t
# 원 하나 그리기
# t.circle(100)

for count in range(10):
    t.circle(100)
    t.left(360/10)

t.mainloop() # t.done 종료

t