'''
    작성일 : 2023/09/20
    작성자 : 202395008
    설명 : 선택문 if~else
           random 를 이용한 가위바위보 게임.
           
           random함수로 생성된 정수를 가지고 게임을 진행합니다.
           0 => 가위
           1 => 바위
           2 => 보
'''
import random

print(":: 가위 바위 보 게임 시작 ::")

num=random.randrange(3)# 0,1,2중 랜덤으로 생성하여 변수에 저장

if num==0:
    print("가위")
if num==1:
    print("바위")
if num==2:
    print("보")

