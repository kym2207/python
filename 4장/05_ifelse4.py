'''
    작성일 : 2023/09/20
    작성자 : 202395008
    설명 : 선택문 if~else
           년도를 입력 받아 윤년인지 아닌지 판단하는 프로그램.
           
           
'''
year=int(input("년도를 입력해 주세요"))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print("윤년입니다.")
        else:
            print("윤년이 아닙니다.")
    else:
        print("윤년입니다.")
else:
    print("윤년이 아닙니다.")
    
    
    
if year%4==0 and year%100!=0 or year%400==0:
    print("윤년입니다.")
else:
    print("윤년이 아닙니다.")