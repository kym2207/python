'''
    작성일 : 2023/09/20
    작성자 : 202395008
    설명 : 선택문 if~else
           random 를 이용한 가위바위보 게임.
           
           random함수로 생성된 정수를 가지고 게임을 진행합니다.
           0 => 가위
           1 => 바위
           2 => 보
           두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행합니다.
'''
import random

print(":: 가위 바위 보 게임 시작 ::")


player1=input("player1의 이름 : ")
player2=input("player2의 이름 : ")
num=random.randrange(3)# 0,1,2중 랜덤으로 생성하여 변수에 저장
num2=random.randrange(3)# 0,1,2중 랜덤으로 생성하여 변수에 저장

#player1의 가위바위보 출력
print(player1,':',end='')
if num==0:
    print("가위")
if num==1:
    print("바위")
if num==2:
    print("보")

#player2의 가위바위보 출력
print(player2,':',end='')
if num2==0:
    print("가위")
if num2==1:
    print("바위")
if num2==2:
    print("보")

#승자 판단하여 출력
if (num==0 and num2==2) or (num==2 and num2==1) or (num==1 and num2==0):
    print(player1,"승리") 
elif (num2==0 and num==2) or (num2==2 and num==1) or (num2==1 and num==0):
    print(player2,"승리") 
else:
    print("무승부")