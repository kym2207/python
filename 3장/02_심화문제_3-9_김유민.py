'''
    작성일 : 2023/09/13
    작성자 : 202395008
    설명 : 90페이지 문제 3-9
        평균시속과 이동시간을 입력받아
        이동 시간은 시,분,초 단위로 출력하고,
        이동한 거리를 계산하여 출려하시오.
'''
km=float(input("평균 시속(km/h)을 입력하세요 : "))
h=float(input("이동 시간(h)을 입력하세요 : "))
print("평균 시속 : {} km/h".format(km))
total_time=h*3600
print("이동 시간 : {:.0f} 시간 {:.0f} 분 {:.0f} 초".format(total_time//3600,(total_time%3600)//60,total_time%60))
print("이동 거리 : {} km".format(km*h))
