# 그외의 연산자들

# 비트연산자
# print(bin(42))
# print(bin(11))

"""
101010
001011
100001

|, &, ^, ~

101010 | 001011
101010 & 001011
~42 = -42 - 1 
~~42 = 42

~42 = -43
~-43 = -(-43) - 1
     = 43 - 1
     = 42
"""

# print(~~42)

# 항등연산자
# id함수 : 값의 메모리 주소
txt = "python"
# print(id(txt))

print(id(1))
print(id('1'))

print(1 == '1')

# 멤버연산자
# in, not in

fruits = ["apple", "banana", "orange"]

print("사과가 있나요? ", "apple" in fruits)
print("딸기가 있나요? ", "strawberry" in fruits)
print("키위는 없나요? ", "kiwi" not in fruits)
