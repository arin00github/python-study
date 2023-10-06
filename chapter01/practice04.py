# STUDY: 제어문(revision)

# STUDY: 1) Boolean
# Boolean 자료형은 비교 연산자의 반환값으로 자주 사용

# a = True
# print(type(a)) # <class 'bool'>
# b = False
# print(type(b)) # <class 'bool'>


# mystock = 'Naver' 
# print(mystock == 'Naver') # True

# day1 = 10000
# day2 = 13000
# gap = (day2 - day1) == (day1 * 0.3)
# print(gap) # True


# STUDY: 2) 논리 연산자
# and 그리고
# or 또는
# 부정 : not ~아닌

cur_price = 9980
check1 = cur_price > 5000 and cur_price < 10000
print(check1) # True

# STUDY: 3) 파이선 if문
# 들여쓰기 위치가 동일해야 함(매우 중요!!!)

naver_cur_price = 9000
if naver_cur_price >= 10000:
    print('Buy naver 10')
else:
    print('Holding')
    
k_price = 7300

if k_price < 1000:
    bid = 1
elif k_price >= 1000 and k_price < 5000:
    bid = 5
elif k_price >= 5000 and k_price < 10000:
    bid = 10
elif k_price >= 10000:
    bid = 20

print(bid) # 10