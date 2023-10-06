import stock


# STUDY : 05. 함수와 모듈

# STUDY : 1) 함수


def print_ntimes(n):
    for i in range(n):
        print('Wake up !')
    

# print_ntimes(2)
# Wake up !
# Wake up !

# 변수가 바인딩하는 값이 실제로 메모리에 저장돼 있다는 개념을 이해
# 할당된 메모리를 자동으로 관리하는 메커니즘을 사용
# 함수 호출 과정에서 할당된 메모리는 함수 호출이 끝나 더는 사용되지 않을 때 자동으로 메모리에서 삭제
def stock_upper(price):
    increment = price * 0.2
    upper_price = increment + price
    return upper_price

# print(stock_upper(277))


def calculate(price):
    offset = price * 0.2
    upper = price + offset
    lower = price - offset
    return (upper, lower)

(upper, lower) = calculate(100000)
# print(upper, lower)


# STUDY : 2) 모듈
# 코드 재사용을 위해 사용

# STUDY : - 1) 모듈만들기

# print(stock.author) # pystock
# print(stock.cal_lower(5000)) # 3500
# print(stock.cal_upper(5000)) # 6500


# STUDY : - 2) 시간 다루기

import time

print(time.time()) # 1696487906.4951441
print(time.ctime()) # Thu Oct  5 15:38:26 2023


# STUDY : - 3) os 모듈

import os

getcwd = os.getcwd() # 현재 경로를 얻을 수 있다

print(getcwd) # D:\00.myarchive\06.python\chapter02

a = dir()
print(a)