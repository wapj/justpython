# 튜플 사용해보기

def return_two_results():
    return 1, 2, 3


def result_something():
    return True, 1, 2, 3


result = return_two_results()

a, b, c = return_two_results()

result2, a, b, c = result_something()

if result2:
    print(a, b, c)

if __name__ == '__main__':
    print(result)
    print(type(result))
    print(a, b, c)

    print(result.index(1))
    print(result.count(1))
    # 주석을 남겨주세요.
    li = list(result)
    print(type(li))
    print(li)


