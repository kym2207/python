'''
    작성일 : 2023/11/01
    작성자 : 202395008
    설명 : lab 7-6 도시의 이름과 인구를 튜플로 묶어보자.
'''
#다음과 같은 리스트가 생성되어 있다
city_info =[('서울',9765),('부산',3441),("인천",2954),('광주',1501),('대전',1531)]
max_population = city_info[0][1] #최대 인구를 구한기 위한 최소값
min_population = city_info[0][1] #최소 인구를 구한기 위한 최대값
total_pop = 0 #모든인구 구하기위한 변수
max_city = None #최대 도시 이름을 저장할 빈 변수
min_city = None #최소 도시 이름을 저장할 빈 변수
for city,population in city_info: #city에 city_info에 있는 값(ex ('서울',9765))를 하나하나 넣으면서 반복
    total_pop += population #모든 도시인구의 합 구하기
    if population > max_population : #가장 인구가 많은 도시 구하기
        max_population = population
        max_city = city
    if population < min_population : #가장 인구가 적은 도시 구하기
        min_population = population
        min_city = city
print('최대인구: {}, 인구: {} 천명'.format(max_city,max_population))
print('최소인구: {}, 인구: {} 천명'.format(min_city,min_population ))
print('리스트 도시 평균 인구: {} 천명'.format(total_pop / len(city_info)))