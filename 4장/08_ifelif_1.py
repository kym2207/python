'''
    작성일 : 2023년9월 27일
    작성자 : 202395008 김유민
    설명 : 점수를 입력받아 학점을 출력하시오.
            90~100 : A학점
            80~89  : B학점
            70~79  : C학점
            60~69  : D학점
            0~59   : F학점
    알고리즘 : 1. 점수를 입력 받는다.
               2. 판단하여 출력한다.
'''
score=int(input("점수입력 : "))
print("::: 첫번째 성적처리 :::")
if score >= 90:
    print("A학점")
elif score >=80:
    print("B학점")
elif score >=70:
    print("C학점")
elif score >=60:
    print("D학점")
else:
    print("F학점")

print()

#정확한 범위를 지정하자. 성적에 벗어난면 잘못된 점수 입력입니다.출력

'''
    90~100 : A학점
    80~89  : B학점
    70~79  : C학점
    60~69  : D학점
    0~59   : F학점
'''
print("::: 두 번째 성적처리 :::")
if(90<=score<=100):
    print("A학점")
elif(score>=80 and score<=89):
    print("B학점")
elif(score>=70 and score<=79):
    print("C학점")
elif(score>=60 and score<=69):
    print("D학점")
elif(score>=0 and score<=59):
    print("F학점")
else:
    print("점수를 잘못 입력하셨습니다.")

#점수는 무조건 0~100점 사이입니다. - 아니면 잘못된 입력입니다.
print("::: 세 번째 성적처리 :::")

if 0<=score<=100:
    if score >= 90:
        print("A학점")
    elif score >=80:
        print("B학점")
    elif score >=70:
        print("C학점")
    elif score >=60:
        print("D학점")
    else: #A,B,C,D학점이 아니면.
        print("F학점")
else: # 0에서 100점 사이의 점수가 아니면
    print("점수를 잘못 입력하셨습니다.")
