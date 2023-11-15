'''
    작성일 : 2023/11/15
    작성자 : 202395008
    설명 : LAB 9-2 : 트위터 메시지 처리의 단어 추출 띄어쓰고로 문자열을 분리하고, 단어의 개수를 찾아라
'''
text = "There's a reason some people are working to make it harder to vote, especially for people of color. It's because when we show up, things change."

# 띄어쓰고로 문자열을 분리하고, 단어의 개수를 찾아라
text2 = text.split()
print(text2)
print('Wordl count : ',len(text2))

#도전문제 9.1
#회사 이름은 **로 표시
# KT,Samsung,LG
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( LG \
U+ Mystic Pink 30%, SKT Mystic Blue not disclosed)'



text2=text.lower()
print(text2.replace('skt',"**").replace('samsung',"**").replace('lg',"**").replace('kt',"**"))
print(text2)


