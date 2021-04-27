# 파이썬 함수 실습


def add(a, b):
    # 더하기
    return a + b


def subtract(a, b):
    # 빼기
    return a - b


def multiply(a, b):
    # 곱하기
    return a * b


def devide(a, b):
    # 나누기
    return a / b


a = 3
b = 5

print("a + b = ", add(a, b))
print("a - b = ", subtract(a, b))
print("a * b = ", multiply(a, b))
print("a / b = ", devide(a, b))


# greeting


def greeting(name):
    # 인사를 하는 함수
    return f"안녕? {name}"


print(greeting("파이썬 그냥 재미로"))


def f_to_c(degree):
    # 화씨를 섭씨로
    return (degree - 32) / 1.8


print("f to c", f_to_c(32))


def c_to_f(degree):
    # 섭씨를 화씨로
    return (degree * 1.8) + 32


print("c to f", c_to_f(0))

import time


def delay_hello(text, sec):
    time.sleep(sec)
    print(text)


delay_hello("안녕하세요~", 10)
