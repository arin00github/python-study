price1 = 1000
price2 = 1000

# id()함수 : 메모리에 할당된 객체의 주소
priceString1 = id(price1)
priceString2 = id(price2)
# print(priceString1) #3182235525136
# print(priceString2) #3182235525136

# 정숫값(Integer) 중 자주 사용할 것 같은 범위의 정숫값은 메모리에 한 번만 올려두고 
# 이를 여러 변수가 가리키게 함으로써 메모리를 효과적으로 사용하려고 함

###
# 3) 파이선 문자열
# - 1) 문자열 인덱싱 및 슬라이싱
mystring = 'hello world'
result = len(mystring)
# print(result) # 11
# print(mystring[6:]) # world
# print(mystring[:5]) # hello


# - 2) 문자열 자르기
my_hobby = "read novel"
print(my_hobby.split(' ')) #공백을 기준으로 분리 ['read', 'novel']

# - 3) 문자열 합치기
daum = "Daum"
kakao = "Kakao"
print(daum + kakao) # DaumKakao
print(daum + ' ' + kakao) # Daum Kakao