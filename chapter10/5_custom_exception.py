class JustError(Exception):

    def __init__(self, error_code, message):
        self.error_code = error_code
        self.message = message


class NegativeNumberError(JustError):
    pass


class ExceedMaxError(JustError):
    pass


def validate(num):
    if num < 1:
        raise NegativeNumberError(1, "양수만 가능합니다.")

    if num > 100:
        raise ExceedMaxError(2, "최대값을 초과했습니다.")


if __name__ == '__main__':
    try:
        validate(0)
    except NegativeNumberError as err:
        code, msg = err.args
        print(f"errcode:{code} | msg: {msg}")

    try:
        validate(101)
    except ExceedMaxError as err:
        print(err)
