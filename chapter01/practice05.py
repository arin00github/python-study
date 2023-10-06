# STUDY: 4) for 문

# for i in [0,1,2,3,4]:
#     print(i)
    
    
# STUDY - 1) for와 range
# range : '범위'라는 의미

# rangeA = range(1, 10)
# print(rangeA) # range(1, 10)
# listA = list(rangeA)
# print(listA) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(1, 5):
#     print(i)
    
# for i in list(range(1,5)):
#     print(i)
    
# 위에 둘 결과는 같음. 다만 메모리 절약 차원에서 range만 쓰는 것이 바람직

# STUDY - 2) for와 리스트

# interest_stock = ['Google', 'Apple', 'Amazon']
# for company in interest_stock:
#     print('%s: Buy 100' % company)


# STUDY - 3) for와 튜플
# 리스트 보다 빠름

# selling_stock = ('LG건강', '금호화학', '대우건설')
# for stock in selling_stock:
#     print('%s: Already Sell 10' % stock)

# STUDY - 4) for와 딕셔너리

# current_stock = {"넥슨": 29300, '롯데건설': 1980, '유한양행': 320500}
# for stock, stock_price in current_stock.items():
#     print('%s: Buy %s' % (stock, stock_price))
# 넥슨: Buy 29300
# 롯데건설: Buy 1980
# 유한양행: Buy 320500


# STUDY: 5) while 문

# STUDY - 1) while문 기초

bankcount = 10000
year = 1
while year < 3:
    bankcount = bankcount * 1.05
    year = year + 1

print(bankcount)

# STUDY - 2) while 과 if

#홀수만 찍어내보기
# num = 0
# while num <= 10:
#     if num % 2 == 1:
#         print(num)
#     num += 1
    
# STUDY - 3) break 과 continue
# 반복문(while 문 또는 for 문)에서 빠져나오려면 break라는 키워드를 사용

# while 1:
#     print('Just Once')
#     break

# #Just Once

# num = 5
# while 1: #무한루프되는 조건
#     print(num)
#     if num == 10:
#         break
#     num += 1

# 파이썬 프로그램이 실행되다가 continue를 만나면 
# 그 아래의 코드를 수행하지 않고 while 문의 조건을 판단하는 곳으로 점프
numA = 0
while numA < 5:
    numA += 1
    if numA == 3:
        continue
    print(numA)

# 3만 출력하지 않음


# STUDY: 6) 중첩 루프
# 중첩 루프(nested loop) : 반복문 여러 개가 겹쳐 있는 구조

for i in range(1,6):
    for j in range(1,3):
        pass # pass 키워드는 아무것도 수행하지 않음을 의미
    
    
apart = [[101, 102, 103],[201, 202, 203],[301, 302, 303]]

for floor in apart:
        for room in floor:
                print("Newspaper delivery: ", room)
                
# Newspaper delivery:  101
# Newspaper delivery:  102
# Newspaper delivery:  103
# Newspaper delivery:  201
# Newspaper delivery:  202
# Newspaper delivery:  203
# Newspaper delivery:  301
# Newspaper delivery:  302
# Newspaper delivery:  303