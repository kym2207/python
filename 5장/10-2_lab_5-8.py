'''
    작성일 : 2023년 10월 4일
    작성자 : 202395008 김유민
    설명 : while문으로 별그리기
            교재 131 페이지
'''
import turtle as t
t.shape("turtle")
i=0
while i < 5:
    t.fd(500)
    t.right(144)
    i+=1

t.mainloop()