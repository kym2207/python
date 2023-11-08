'''
    작성일 : 2023/11/08
    작성자 : 202395008
    설명 : LAB 8-6 튜플 요소로 가지는 student_tuple 리스트가 다음과 같이 있다.
                   이 튜플의 요소가 되는 튜플은 (학번, 이름, 전화번호)로 이루어져 있다.
                   1. 이를 이용하여 (학번:이름)의 딕셔너리를 만들어 출력하여라.
                   2. 이를 이용하여 학번으로 조회를 할 경우 다음과 같이 학번, 이름과 전화번호가 출력되도록 하여라.
'''
student_tuple = [("211101",'강이안', '010-123-1111'),("211102",'박동민', '010-123-2222'),("211103",'김수정', '010-123-3333')]
student_dict={}
#1. 이를 이용하여 (학번:이름)의 딕셔너리를 만들어 출력하여라.
for id_num,name, phone in student_tuple :
    student_dict[id_num]= [name,phone]
for key, value in student_dict.items():
    print(key,":",value[0])

# 2. 이를 이용하여 학번으로 조회를 할 경우 다음과 같이 학번, 이름과 전화번호가 출력되도록 하여라.
number = input("학번을 입력하시오 : ")
print(f"{number} 학생은 {student_dict[number][0]}이며, 전화번호는 {student_dict[number][1]}입니다.")