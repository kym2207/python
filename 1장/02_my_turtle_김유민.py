'''
    작성일 : 2023/09/13
    작성자 : 김유민
    설명 : 터틀 그리기
'''
import turtle as t #터틀 모듈을 사용하기 위한 준비
                   #turtle 클래스 객체를 t로 생성. (별명)
t.shape('turtle')
t.speed(2000)
#선그리기
#t.forward(200)  #200 픽셀이동.

#삼각형 그리기
# for i in range(10):
#     t.forward(200)#200픽셀 이동
#     t.left(360/10)#120도 회전
# for i in range(5):
#     t.forward(200)#200픽셀 이동
#     t.left(144)#120도 회전
for i in range(720):  # 360번 반복
    t.fd(i)
    t.right(91)  

t.mainloop()