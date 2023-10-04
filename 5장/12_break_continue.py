'''
    작성일 : 2023년 10월 4일
    작성자 : 202395008 김유민
    설명 : 반복문을 제어하는 break, continue
           교재 137페이지

    Text word : programming
'''
word = input("단어를 입력하세요 : ")

print(":: break ::")
for i in word:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' : #모음을 만나면 반복 중지.
        break
    else:
        print(i,end='')
#pr o에서 break 하여 o를 출력하지않고 for문을 빠져나와서

print()

print(":: break2 ::")
for i in word:
    if i in ['a','e','i','o','u','A','E','I','O','U'] : #모음을 만나면 반복 중지.
        break
    else:
        print(i,end='')

print()

print(":: continue ::")
for i in word:
    if i in ['a','e','i','o','u','A','E','I','O','U'] :#모음을 만나면 넘어감.
        continue#반복의 처음으로 돌아간다. 아래 문장을 만날 수 없다.
    print(i,end='')#prgrmmn