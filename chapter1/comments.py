def say_hello():
    print("안녕하세요~")


class Greeter:
    """
    인사에 관련된 처리를 하는 클래스
    say_안녕
    say_hello
    say_こんにちは
    함수를 가지고 있다.
    """

    def __init__(self):
        print("[ 클래스 ] 안녕하세요~")

Greeter()
