'''
    작성일  : 2023/09/13
    작성자  : 김유민
    설명    : 피자의 면적을 구하시오.
              피자의 반지름이 필요하다.
              피자의 반지름은 입력 받아 계산한다.
'''
r=int(input("반지름을 입력해주세요. : "))
print("반지름이 {}인 피자의 면적은 {:.2f}입니다.".format(r,3.14*r**2))
