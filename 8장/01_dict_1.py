'''
    작성일 : 2023/11/01
    작성자 : 202395008
    설명 : 8.1 키와 값을 가지는 딕서너리

    튜플 =()  리스트 = []  딕셔너리 = {}
'''
# 빈 딕셔너리 생성
phone_book1 = {}

#딕셔너리에 값 저장. key, value [key] = value
phone_book1['김유민'] = '010-2338-3616'

print("phone_book1 :",phone_book1) # {'김유민': '010-2338-3616'}

#딕셔너리에 값 저장. 2. {ket : value}
phone_book2= {'홍길동' : '010-7899-4545', '김유민' : '010-2338-3616'}
print('phone_book2 :',phone_book2)

phone_book3 = {}
phone_book3['김유민'] = '010-2338-3616'
phone_book3['천승용'] = '010-7640-2671'
phone_book3['김경현'] = '010-9932-8517'
phone_book3['홍길동'] = '010-1234-1234'
phone_book3['일순신'] = '010-4321-9876'

print("phone_book3 :",phone_book3)

print()

print(":: 전화번호 phone_book3 출력 ::")
#모든 key 출력
print(phone_book3.keys())
#모든 value 출력
print(phone_book3.values())
#모든 key,value 출력
print(phone_book3.items())

print()
print(":: 전화번호 phone_book3 itmes()출력 ::")
for name,phone_num in phone_book3.items():
    print(name,':',phone_num)

print()
print(":: 전화번호 phone_book3[key]로 접근하여 출력 ::")
for key in phone_book3.keys():
    print(key,':',phone_book3[key])

print()

print("딕셔너리 작성 시 :(콜론)을 기준으로 key:value 작성")
person_dist = {'name' : '김유민','age' : 19, 'class' : '1학년'}

print('name :',person_dist['name'])
print('age :',person_dist['age'])
print('class :',person_dist['class'])

print()

print(":: 정렬 ::")
#phone_book3 를 정렬
#딕셔너리를 키를 기준으로 정렬하여 리스트로 변환
print(sorted(phone_book3))

print(":: 키를 기준으로 전체 정렬 ::")
sort_phone_book3=sorted(phone_book3.items(), key=lambda x: x[0])
print(sort_phone_book3)

print(":: 값을 기준으로 정렬 ::")
sort_phone_book3=sorted(phone_book3.items(), key=lambda x: x[1])
print(sort_phone_book3)

print()

print(":: 항목 삭제 ::")
del phone_book3['김유민']
print(phone_book3)

print(":: 전체 삭제 ::")
phone_book3.clear()
print(phone_book3)