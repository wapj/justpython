"""
% 를 사용하기
%s : 문자열
%i : 숫자
"""

name = "승규"
age = str(38)  # '38'
test = "안녕 %s %s" % (name, age)
# print(test)

# string format method
"""
타입에 관계없이 넣을 수 없나?
파이썬 3부터 가능 format() 함수를 사용하자.
사용법은 "문자열".format(*args, **kwargs)

*args 라고 하는 것은 
'{} {} {} {}....{}'.format('param1', 2, 'param3', ... , paramN) 
이런 식으로 파라메터를 여러개 넣을 수 있다는 의미
중괄호 {} 는 파라메터 갯수만큼 넣을 수 있으며 적어도 상관없으나 많으면 IndexError 가 나게됨. 

**kwargs 라고 하는 것은 
'{key1} {key2} {key3}'.format(key1='a', key2='b', key3=3) 
이런식으로 파라메터의 키와 값이 같이 있는 형태를 말함
*args 와 마찬가지로 키에 있는 값이 덜 들어가는 것은 괜찮지만, 
모르는 키가 들어가면 KeyError 가 나게 된다.

% 를 사용하는 방법보다는 좋아졌지만, 
여전히 문자열과 파라메터의 갯수혹은 키가 맞지 않으면 에러가 나게 될 가능성이 있고, 
파라메터가 많아지면 많아질수록 스트링과 format 함수의 값을 맞추는 것이 힘들어진다.     
"""

version = 3
function_name = "format()"
# print("파이썬 {0}부터 가능 {1} 함수를 사용하자.".format(version, function_name))
# print("{key1} {key2} {key3}".format(key1="문자열", key2="문자열2", key3=3))

txt1 = "울릉도"
txt2 = "동남쪽"
txt3 = "뱃길따라"
txt4 = "87k"
txt5 = "외로운"
txt6 = "섬하나"
txt7 = "새들의 고향"

"""
f-strings 
PEP-0498 (파이썬 개선을 위한 제안서 498번)에 제안되고 3.6에 적용됨
https://www.python.org/dev/peps/pep-0498/
"""

# print(f"{txt1} {txt2} {txt3} {txt4} {txt5} {txt6} {txt7}")

# expression : 표현식, statement : 구문
# 값으로 표현될 수 있는 것

answer = 40 + 2


def add(a, b):
    """
    더하기를 하는 함수
    :param a:
    :param b:
    :return:
    """
    return a + b


answer2 = add(41, 1)

fn = add

# print(f"{42 + 1}")
# print(f"{add(10, 10)}")
# print(f"{add}")
# print(f"{add.__doc__}")


"""
포맷스트링 스펙 format()
[[fill]align][sign][#][0][minimumwidth][,][.precision][type]

fill : 아무런문자나가능
align : <, ^, >
sign : +, -
minimumwidth: 양수
# : 타입이 실수인데 정수인 경우 소수점을 생략하지 않음
0 : 남는 것은 0으로 채우고 오른쪽정렬 (즉 0> 와 동일)
, : 3자리마다 콤마 표시.
precision : .2 는 소수점 2자리까지 표시
type : b, c, d, e, E, f, F, g, G, n ,o, s, x, X, %
"""


def fstring1():
    for x in range(10):
        n = x + 1
        print(f"{n:010} ** {n:0>2} = {n ** n:$>%}")


# fstring1()

# print(f"{'string':s}")

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름은 {self.name}이고, 나이는 {self.age}입니다."

    def __repr__(self):
        return f"name : {self.name} | age {self.age}"


my = Person("승규", 38)
# print(f"{my!r}")

title = "파이썬 그냥 재미로"
use_time = 30
intro_just_python = f"""{title} 강의에서는
파이썬의 기초를 탄탄하게 다져줍니다. 
하루에 {use_time:$>10}분만 투자하시면 
어느새 나도 파이썬 개발자!"""


# print(intro_just_python)


def deco_str(val):
    return f"""{'=' * 30}
{val}
{'=' * 30}
"""

#print(deco_str(intro_just_python))

a = "a"
b = "b"
c = 10

print(f"{a} {b} {c}")
print("{}".format(a) + " " + "{}".format(b) + " " + "{}".format(c))







