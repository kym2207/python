'''
    작성일 : 2023/11/08
    작성자 : 202395008
    설명 : LAB 8-5 파티 동시 참석자 알아내기
'''
partyA = set(["Park","Kim","Lee"])
partyB = set(["Park","choi"])

print("파티 A, B에 모두 참석한 사람들 :",partyA.intersection(partyB))

print("파티 A, B에 참석한 사람들 :",partyA.union(partyB))

print("파티 A, B에 중복없이 참석한 사람 :",partyA.symmetric_difference(partyB))

print("파티 A에만 참석한 사람 :",partyA.difference(partyB))

