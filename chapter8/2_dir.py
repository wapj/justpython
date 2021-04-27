# dir 모듈, 패키지, 함수, 클래스

# for x in dir(random):
#     if not x.startswith('_'):
#         print(x)

class Test:
    """
    테스트 클래스입니다.
    """
    class_val = "클래스 더미 변수"

    def dummy(self):
        """
        더미 함수입니다.
        :return:
        """
        return "TEST"

    def dummy2(self, a, b):
        return a + b


help(Test)

import dataclasses
help(dataclasses)