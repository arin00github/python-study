# STUDY: 파이선 기본 구조 자료


interest1 = '삼성전자'
interest2 = '네이버'
interest3 = 'LG전자'
 
# 변수가 실제 데이터가 존재하는 위치를 가리키고 있는 것을 바인딩(binding)한다고 표현


# STUDY:  1. 리스트
# 여러 개의 데이터를 ‘순서대로’ 저장하고 이를 관리해야 할 때 사용 됨
interest = ['삼성전자', '네이버', 'LG전자']

# STUDY: 1) 리스트 인덱싱
# print(interest[0])
# print(interest[-1]) # [-1]은 리스트의 데이터 중 맨 마지막에 있는 데이터를 의미

# STUDY: 2) 리스트 슬라이싱
kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']
# print("시가총액 5위: ", kospi_top10[4])
kospi_top5 = kospi_top10[0:5]
# print(kospi_top5)
# print(kospi_top10[5:-1]) # ['제일모직', '삼성전자우', '삼성생명', 'NAVER']
# print(kospi_top10[5:9]) # ['제일모직', '삼성전자우', '삼성생명', 'NAVER']
# print("before append :", kospi_top10)

# STUDY:  3) 리스트에 데이터 삽입하기
# kospi_top10.append('SK텔레콤')
# print("after append :", kospi_top10) # SK텔레콩이 추가 됨
# kospi_top5.insert(2, '카카오')
# print('after insert', kospi_top5) # 3번째에 '카카오'가 추가됨

# STUDY:  4) 리스트 데이터 삭제
# print(len(kospi_top10)) # 10
# del kospi_top10[-1] # 해당 데이터 삭제 됨
# print(len(kospi_top10)) # 9



# STUDY:  2. 튜플
# 튜플은 리스트에 있는 여러 기능이 빠져 있고, 반대로 리스트는 튜플이 지원하는 모든 기능을 포함
# 튜플은 리스트보다 속도가 빠르다는 장점이 있다
# 한번 데이터를 저장해둔 후 추가하거나 삭제할 필요가 없는 경우라면 되도록 리스트보다는 튜플을 사용하는 것이 좋음
# 인덱싱을 통해 튜플의 원소에 접근 가능함
# 튜플은 리스트와 달리 원소를 수정할 수 없으므로 원소의 내용을 바꾸려고 하면 에러가 발생

t = ('Samsung', 'LG', 'Doosan')
# print(t) # ('Samsung', 'LG', 'Doosan')

# t[0] = 'Apple' # 실행불가. 에러가 발생함

# print(t[0:2]) # ('Samsung', 'LG')


# STUDY:  3. 딕셔너리
# 키(key)와 값(value)이라는 것을 쌍으로 저장함으로써 더 쉽게 저장된 값을 찾을 수 있는 구조
# 딕셔너리는 리스트와 튜플과 달리 인덱싱을 지원하지 않음
# 데이터를 순서대로 저장하는 것이 아니라 키와 값의 쌍이 서로 연결되도록만 저장되기 때문

cur_price = {}
print(type(cur_price)) # <class 'dict'>
cur_price['hanabank'] = 12000
# print(cur_price) # {'hanabank': 12000}
cur_price['kb_bank'] = 13000
# print(len(cur_price)) # 2
# print(cur_price['hanabank']) # 12000

# STUDY:  1) 딕셔너리에 데이터 삽입 및 삭제

cur_price['lotte'] = 3400
del cur_price['kb_bank']
print(cur_price) # {'hanabank': 12000, 'lotte': 3400}
print(cur_price.keys()) # dict_keys(['hanabank', 'lotte'])

# STUDY: 2) 딕셔너리로부터 키-값 구하기

# 순수하게 목록만 구하기
list_key_price = list(cur_price.keys()) 
print(list_key_price) # ['hanabank', 'lotte']
# 순수하게 값만 구하기
list_value_price = list(cur_price.values())
print(list_value_price)

check1 = 'Samsung' in cur_price.keys()
print(check1) # False

check2 = 'lotte' in cur_price.keys()
print(check2) # True