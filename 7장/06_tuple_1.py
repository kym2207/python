'''
    작성일 : 2023/11/01
    작성자 : 202395008
    설명 : 한번 생성하면 그값을 고칠 수 없는 자료형 : 튜플
'''
#리스트 생성
color_list=['red','green','blue','orange']

#튜플 생성
color=('red','green','blue','orange')

#튜플 출력
print(f"color : {color}")

#color에 black추가하기
# color.append('black')#AttributeError: 'set' object has no attribute 'append' // append 속성이 없음 튜플에

#인덱싱과 슬라이싱은 문자열이나 리스트와 동일하게 동작한다
print("color 튜플 : ",color)
print("color 튜플 중 2,3,4번은? ",color[1:4])#슬라이싱
print("color 튜플 중 1,2,3번은? ",color[:3])
print("color 튜플 중 3~끝은? ",color[2:])
print("color 튜플 중 1,3,5번은? ",color[::2])#2씩 증가하면서 출력
print("color 튜플 거꾸로 출력 ",color[::-1])

print()
#튜플 끼리의 결합 => + 연산자. 반복 => * 연산자

colors=color+color
print("colors 튜플 : ",colors)
print("color 튜플을 10번 반복: ",color*10)


