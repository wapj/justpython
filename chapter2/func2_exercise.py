"""
- 파이썬에서 제곱은 a **2 로 표현됩니다.
  어떤 숫자를 넘기면 제곱을 리턴하는 함수 square를 만들어봅시다.
"""

# ctrl + cmd + b


def square(a):
    return a ** 2


# print(square(3))
"""
- 밑변과 높이를 넣으면 삼각형의 넓이를 구해주는 함수를 만들어봅시다.
  삼각형 넓이는 밑변 x 높이 / 2 입니다.
  파라메터를 두개 받는 함수를 만들어 봅시다.
"""


def triangle(width, height):
    return width * height / 2


# print(triangle(10, 5))

"""
- 1달러환율이 1120원이라 가정하고 원을 넣으면
  달러로 바꾼뒤 출력해주는 함수를 만들어봅시다.
  round(숫자, 2) 를 사용하여 소수점 둘째 자리까지 나오도록 처리해봅시다. 
"""


def to_dollar(won):
    # 1달러 : 1120원
    # 1원 : 1/1120 달러
    return round(won / 1120, 2)


# print(to_dollar(1120))


"""
- 주문정보(음료이름, 사이즈, 아이스여부, 수량) 를 넣으면
  주문정보를 출력해주는 함수
  order(name, size, is_ice, amount) 를 만들어 봅시다.
  order는 매개변수값으로 받은 정보를 return을 사용하여
  똑같이 리턴 해주어야합니다. 그 정보를 print 로 출력해봅시다.
"""


def order(name, size, is_ice, amount):
    print(f"주문정보 name : {name} | size : {size} | is_ice : {is_ice} | amount : {amount}")
    return name, size, is_ice, amount


"""
- 주문정보(음료이름, 사이즈, 아이스여부, 수량) 받아서
  커피를 만드는 make_coffee(name, size, is_ice, amount)
  함수를 만들고 "주문하신 {name} {size}사이즈 {is_ice} {amount} 잔 나왔습니다." 가
  출력되도록 해봅시다.
"""


def make_coffee(name, size, is_ice, amount):
    print(f"주문하신 {is_ice} {name} {size}사이즈  {amount} 잔 나왔습니다.")


make_coffee("아메리카노", "톨", "따뜻한", 2)
