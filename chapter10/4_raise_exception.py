# 에러를 발생시키는 방법
# raise Exception("메세지")

def is_boolean(a):
    if not isinstance(a, bool):
        raise ValueError("유효성 검증 실패!")
    return True


# raise Exception from OriginalError

def dirty(num):
    """누군가 만들어둔 함수 근데 수정불가!"""
    if num > 100:
        raise Exception("그냥 에러!")


def clean(num):
    try:
        return dirty(num)
    except Exception as err:
        raise ValueError("유효성 검증 실패") from err


def validate(num):
    if num < 1:
        raise ValueError("양수만 가능합니다.")

    if num > 100:
        raise ValueError("100보다 클수 없습니다.")

    try:
        print(num + " ")
    except TypeError as err:
        raise ValueError("타입에러지만 Value에러로 처리") from err


if __name__ == '__main__':
    try:
        validate(-1)
    except ValueError as err:
        print(err)

    try:
        validate(101)
    except ValueError as err:
        print(err)

    try:
        validate(10)
    except ValueError as err:
        print(err)

